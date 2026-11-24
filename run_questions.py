"""평가 질문을 graphrag global 검색으로 일괄 실행하고, 응답과 근거 기록을 파일로 남긴다.

예)
  python run_questions.py --dry-run                        # API를 부르지 않고 계획과 예상 비용만 본다
  python run_questions.py --only Q03 Q05 --level 0         # 일부만, 싼 설정(0층)으로
  python run_questions.py                                  # 30문항 전부, 2층 (약 11달러 예상)
  python run_questions.py --out results/20261124-1530_L2   # 중단된 실행을 이어서 (끝난 문항은 건너뛴다)

결과는 results/<시각>_L<층>/ 에 남는다.
  answers.md        사람이 읽는 기록: 질문, 응답, 인용한 보고서, 정답(채점 기준)
  summary.csv       문항별 한 줄 요약 (엑셀로 열 수 있다)
  records/Q05.json  문항별 전체 기록: 실제로 보낸 프롬프트, 응답, 묶음별 보고서 번호, 점수가 붙은 핵심 문장
  run.json          실행 조건과 합계

보내는 프롬프트는 docs/questions_b_2001.md의 공통 지시문 + 유형별 지시문 + 질문이다.
정답(docs/questions_b_2001_evidence.md)은 answers.md에만 붙이고 모델에는 보내지 않는다.
이 스크립트는 `graphrag query --method global`과 같은 api.global_search를 부른다.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import io
import json
import re
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path

csv.field_size_limit(10_000_000)

HERE = Path(__file__).resolve().parent

# 비용 추정용 단가. 2026-11-24에 질문 4번(대부분 2층 질문 1개)을 돌린 뒤 OpenAI 콘솔 누적 0.4달러를
# query.log의 토큰 합계(371만)로 나눈 값이다. 프롬프트 캐시가 없을 때의 단독 실행 단가라서,
# 같은 보고서 묶음을 연속으로 돌리면 실제 청구액은 이보다 훨씬 낮다
# (같은 날 30문항 연속 실행: 이 단가로는 약 11.7달러, 콘솔 실제는 약 3.4달러).
DEFAULT_USD_PER_MTOK = 0.108
# 같은 날 측정: 2층(보고서 4,036개) 질문 하나의 입력이 약 343만 토큰이었다. 드라이런 예상에만 쓴다.
TOKENS_PER_REPORT = 850

# graphrag가 모든 map 응답의 점수가 0일 때 돌려주는 정형 문장의 앞부분
NO_DATA_PREFIX = "I am sorry but I am unable to answer this question"

ROW = re.compile(r"^\|\s*(Q\d{2})\s*\|")
CITE_BLOCK = re.compile(r"\[Data:\s*([^\]]*)\]")
CITE_GROUP = re.compile(r"([A-Za-z]+(?: [A-Za-z]+)*)\s*\(([^)]*)\)")

STATUS_KO = {"answered": "응답", "no_data": "답 없음(정형 문장)"}


# ───────────────────────── 문서 파싱 ─────────────────────────

def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_questions(path: Path) -> tuple[str, list[dict]]:
    """질문 문서에서 공통 지시문과 문항(ID, 주제, 질문, 소속 유형, 유형별 지시문)을 뽑는다."""
    text = path.read_text(encoding="utf-8")
    common = ""
    m = re.search(r"\*\*공통 지시문\*\*\s*\n+((?:>.*(?:\n|$))+)", text)
    if m:
        common = " ".join(re.sub(r"^>\s?", "", ln).strip() for ln in m.group(1).splitlines()).strip()

    questions: list[dict] = []
    section, section_instr, want_instr = "", "", False
    for ln in text.splitlines():
        if ln.startswith("## "):
            section = ln[3:].split("·")[0].strip()
            section_instr, want_instr = "", True
        elif ROW.match(ln):
            cells = split_row(ln)
            if len(cells) >= 3:
                questions.append({
                    "id": cells[0],
                    "topic": cells[1],
                    "question": " | ".join(cells[2:]),
                    "section": section,
                    "section_instruction": section_instr,
                })
        elif want_instr and ln.strip() and not ln.startswith(("|", ">", "#")):
            section_instr, want_instr = ln.strip(), False
    return common, questions


def parse_answer_key(path: Path) -> dict[str, dict]:
    """정답 문서의 표에서 문항별 정답과 원문 근거 번호를 뽑는다. 채점 기록용이며 모델에는 보내지 않는다."""
    if not path.exists():
        return {}
    key: dict[str, dict] = {}
    for ln in path.read_text(encoding="utf-8").splitlines():
        if ROW.match(ln):
            cells = split_row(ln)
            if len(cells) >= 4:
                key[cells[0]] = {"answer": " | ".join(cells[2:-1]), "evidence": cells[-1]}
    return key


def select_questions(questions: list[dict], only: list[str] | None) -> list[dict]:
    if not only:
        return questions
    wanted: set[str] = set()
    for tok in only:
        tok = tok.upper().replace("Q", "")
        try:
            if "-" in tok:
                a, b = tok.split("-", 1)
                nums = range(int(a), int(b) + 1)
            else:
                nums = [int(tok)]
        except ValueError:
            sys.exit(f"--only 형식이 잘못됐다: {tok!r} (예: Q03 Q05 또는 Q01-Q10)")
        wanted.update(f"Q{n:02d}" for n in nums)
    known = {q["id"] for q in questions}
    missing = sorted(wanted - known)
    if missing:
        sys.exit(f"질문 문서에 없는 문항: {', '.join(missing)}")
    return [q for q in questions if q["id"] in wanted]


def build_prompt(q: dict, common: str, plain: bool) -> str:
    if plain:
        return q["question"]
    guide = "\n".join(p for p in (common, q["section_instruction"]) if p)
    return f"[답변 지침]\n{guide}\n\n[질문]\n{q['question']}"


# ───────────────────────── 응답 분석 ─────────────────────────

def parse_citations(text: str) -> dict:
    """응답 속 [Data: Reports (1, 2, +more); Entities (3)] 에서 종류별 번호를 뽑는다."""
    found: dict[str, list[int]] = {}
    more = False
    for block in CITE_BLOCK.findall(text):
        for kind, body in CITE_GROUP.findall(block):
            more = more or "+more" in body
            lst = found.setdefault(kind.strip(), [])
            for n in (int(x) for x in re.findall(r"\d+", body)):
                if n not in lst:
                    lst.append(n)
    return {"by_kind": found, "has_more": more}


def batch_report_ids(chunk: str) -> list[int]:
    """map 단계 한 묶음의 컨텍스트(CSV, 구분자 |)에서 보고서 번호를 읽는다."""
    ids: list[int] = []
    for row in csv.reader(io.StringIO(chunk), delimiter="|"):
        if row and row[0].strip().isdigit():
            ids.append(int(row[0]))
    return ids


def make_collector():
    """검색 도중의 묶음 컨텍스트, map 응답, 컨텍스트 레코드를 모으는 콜백."""
    from graphrag.callbacks.noop_query_callbacks import NoopQueryCallbacks

    class Collector(NoopQueryCallbacks):
        def __init__(self) -> None:
            super().__init__()
            self.chunks: list[str] = []
            self.map_results: list = []
            self.context = None

        def on_map_response_start(self, map_response_contexts) -> None:
            self.chunks = list(map_response_contexts)

        def on_map_response_end(self, map_response_outputs) -> None:
            self.map_results = list(map_response_outputs)

        def on_context(self, context) -> None:
            self.context = context

    return Collector()


def build_record(q: dict, prompt: str, response, context, collector, seconds: float, started: str,
                 settings: dict, usd_per_mtok: float) -> dict:
    if not isinstance(response, str):
        response = json.dumps(response, ensure_ascii=False)

    batches, key_points = [], []
    n_failed = n_unparsed = 0
    for i, r in enumerate(collector.map_results):
        resp = r.response if isinstance(r.response, list) else []
        pts = [
            {"analyst": i + 1, "score": int(p["score"]), "answer": p["answer"]}
            for p in resp
            if isinstance(p, dict) and isinstance(p.get("score"), (int, float)) and p["score"] > 0
        ]
        key_points.extend(pts)
        # 호출이 예외로 실패하면 graphrag는 오류를 삼키고 점수 0으로 대체한다. 이때 출력 토큰이 0이다.
        failed = r.output_tokens == 0
        unparsed = (not failed) and resp == []
        n_failed += failed
        n_unparsed += unparsed
        batches.append({
            "index": i + 1,
            "report_ids": batch_report_ids(collector.chunks[i]) if i < len(collector.chunks) else [],
            "n_key_points": len(pts),
            "prompt_tokens": r.prompt_tokens,
            "output_tokens": r.output_tokens,
            "seconds": round(r.completion_time, 2),
            "failed": bool(failed),
            "unparsed": bool(unparsed),
        })
    key_points.sort(key=lambda p: -p["score"])

    ctx_ids: list[int] = []
    if isinstance(context, dict) and "reports" in context:
        try:
            ctx_ids = [int(x) for x in context["reports"]["id"]]
        except Exception:
            ctx_ids = []

    est_prompt = sum(b["prompt_tokens"] for b in batches)
    est_output = sum(b["output_tokens"] for b in batches)
    warnings = []
    if n_failed:
        warnings.append(f"map 호출 {n_failed}개가 실패해 점수 0으로 처리됐다. 응답이 불완전할 수 있다. enron/logs/query.log를 확인.")
    if n_unparsed:
        warnings.append(f"map 응답 {n_unparsed}개를 해석하지 못했다.")

    return {
        "id": q["id"],
        "topic": q["topic"],
        "section": q["section"],
        "question": q["question"],
        "prompt": prompt,
        "settings": settings,
        "started_at": started,
        "seconds": round(seconds, 1),
        "status": "no_data" if response.strip().startswith(NO_DATA_PREFIX) else "answered",
        "response": response,
        "cited": parse_citations(response),
        "context": {
            "n_reports": len(ctx_ids),
            "n_batches": len(batches),
            "n_batches_failed": int(n_failed),
            "n_batches_unparsed": int(n_unparsed),
            "n_key_points": len(key_points),
        },
        "key_points": key_points,
        "batches": batches,
        "usage_estimate": {
            "prompt_tokens": est_prompt,
            "output_tokens": est_output,
            "cost_usd": round((est_prompt + est_output) / 1e6 * usd_per_mtok, 4),
            "note": "map 단계 호출의 토큰 추정치. reduce 단계는 포함하지 않는다.",
        },
        "warnings": warnings,
    }


# ───────────────────────── 파일 출력 ─────────────────────────

def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_records(out_dir: Path) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((out_dir / "records").glob("Q??.json"))]


def render_answers_md(run: dict, records: list[dict], key: dict, rep_index: dict) -> str:
    s, t = run["settings"], run["totals"]
    L = ["# 질문 응답 기록", ""]
    L.append(f"- 실행: {run['created_at']} (갱신 {run['updated_at']})")
    L.append(
        f"- 설정: 층 {s['community_level']} · 동적 선택 {'켬' if s['dynamic'] else '끔'} · 응답 형식 {s['response_type']} · "
        f"{'질문만 전송' if s['plain'] else '공통 지시문 + 유형별 지시문 + 질문 전송'} · 모델 {s['model']}"
    )
    L.append(f"- 진행: {t['done']} / {run['n_selected']}문항 기록 (응답 {t['answered']}, 답 없음 {t['no_data']})")
    L.append(
        f"- 추정 사용량: 입력 {t['est_prompt_tokens']:,} · 출력 {t['est_output_tokens']:,} 토큰 ≈ ${t['est_cost_usd']:.2f} "
        "(map 단계 토큰 × 캐시 없는 단가 기준 추정이라 캐시가 적용되면 실제는 더 낮다. 정확한 금액은 OpenAI 콘솔)"
    )
    L.append("- 응답의 `[Data: Reports (n)]`에서 n은 커뮤니티 보고서 번호다 (community_reports.parquet의 community 열).")
    L += ["", "| ID | 주제 | 상태 | 인용 보고서 수 |", "|---|---|---|---|"]
    for r in records:
        n_cited = len(r["cited"]["by_kind"].get("Reports", []))
        L.append(f"| {r['id']} | {r['topic']} | {STATUS_KO[r['status']]} | {n_cited} |")
    L.append("")

    for r in records:
        c = r["context"]
        L.append(f"## {r['id']} · {r['topic']}")
        L.append("")
        L.append(
            f"*{r['section']} · {STATUS_KO[r['status']]} · {r['seconds']:.0f}초 · 읽은 보고서 {c['n_reports']:,}개 · "
            f"묶음 {c['n_batches']}개 · 점수 붙은 핵심 문장 {c['n_key_points']}개*"
        )
        for w in r["warnings"]:
            L += ["", f"> ⚠ {w}"]
        L += ["", "**질문**", "", f"> {r['question']}", "", "**응답**", ""]
        L += [f"> {ln}" if ln.strip() else ">" for ln in r["response"].splitlines()]
        cited = r["cited"]["by_kind"].get("Reports", [])
        if cited:
            L += ["", "**응답이 인용한 보고서**" + (" (목록 일부 생략: +more)" if r["cited"]["has_more"] else ""), ""]
            for cid in cited:
                lv, title = rep_index.get(cid, (None, "(보고서 정보 없음)"))
                L.append(f"- {cid} · {'L' + str(lv) if lv is not None else '?'} · {title}")
        k = key.get(r["id"])
        if k:
            L += ["", "**정답 (채점 기준)**", "", f"> {k['answer']}", "", f"원문 근거 번호(연간 CSV): {k['evidence']}"]
        L.append("")
    return "\n".join(L) + "\n"


def write_summary_csv(path: Path, records: list[dict]) -> None:
    cols = ["id", "section", "topic", "status", "seconds", "n_reports", "n_batches", "n_batches_failed",
            "n_key_points", "n_cited_reports", "cited_reports", "est_prompt_tokens", "est_output_tokens",
            "est_cost_usd", "response_chars"]
    with path.open("w", encoding="utf-8-sig", newline="") as f:  # BOM: 엑셀에서 한글이 깨지지 않게
        w = csv.writer(f)
        w.writerow(cols)
        for r in records:
            cited = r["cited"]["by_kind"].get("Reports", [])
            c, u = r["context"], r["usage_estimate"]
            w.writerow([r["id"], r["section"], r["topic"], r["status"], r["seconds"], c["n_reports"], c["n_batches"],
                        c["n_batches_failed"], c["n_key_points"], len(cited), " ".join(map(str, cited)),
                        u["prompt_tokens"], u["output_tokens"], u["cost_usd"], len(r["response"])])


def finalize(out_dir: Path, run: dict, key: dict, rep_index: dict) -> dict:
    """records/ 를 읽어 run.json, summary.csv, answers.md 를 다시 만든다. 중간에 멈춰도 그때까지의 기록이 보인다."""
    records = load_records(out_dir)
    run["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
    run["totals"] = {
        "done": len(records),
        "answered": sum(r["status"] == "answered" for r in records),
        "no_data": sum(r["status"] == "no_data" for r in records),
        "est_prompt_tokens": sum(r["usage_estimate"]["prompt_tokens"] for r in records),
        "est_output_tokens": sum(r["usage_estimate"]["output_tokens"] for r in records),
        "est_cost_usd": round(sum(r["usage_estimate"]["cost_usd"] for r in records), 2),
        "seconds": round(sum(r["seconds"] for r in records), 1),
    }
    write_json(out_dir / "run.json", run)
    write_summary_csv(out_dir / "summary.csv", records)
    (out_dir / "answers.md").write_text(render_answers_md(run, records, key, rep_index), encoding="utf-8")
    return run["totals"]


# ───────────────────────── graphrag 로딩과 실행 ─────────────────────────

def load_graph(root: Path, data: Path | None):
    """graphrag query 명령과 같은 방식으로 설정과 인덱스 표를 읽는다. (load_config는 작업 폴더를 root로 바꾼다.)"""
    from graphrag.config.load_config import load_config
    from graphrag.data_model.data_reader import DataReader
    from graphrag_storage import create_storage
    from graphrag_storage.tables.table_provider_factory import create_table_provider

    overrides = {"output_storage": {"base_dir": str(data)}} if data else {}
    config = load_config(root_dir=root, cli_overrides=overrides)
    reader = DataReader(create_table_provider(config.table_provider, storage=create_storage(config.output_storage)))
    tables = {n: asyncio.run(getattr(reader, n)()) for n in ("entities", "communities", "community_reports")}
    return config, tables


def model_info(config) -> dict:
    """모델 이름과 호출 옵션만 꺼낸다. 설정 전체를 덤프하지 않는다 (API 키가 들어 있다)."""
    try:
        m = config.get_completion_model_config(config.global_search.completion_model_id)
        return {"model": m.model, "call_args": dict(m.call_args or {})}
    except Exception:
        return {"model": "unknown", "call_args": {}}


def count_reports(tables: dict, level: int) -> int:
    from graphrag.query.indexer_adapters import read_indexer_reports

    return len(read_indexer_reports(tables["community_reports"].copy(), tables["communities"].copy(),
                                    community_level=level, dynamic_community_selection=False))


async def run_all(args, config, tables, todo, common, out_dir: Path, settings: dict, finalize_cb) -> None:
    import graphrag.api as api

    consecutive_errors = 0
    for n, q in enumerate(todo, 1):
        prompt = build_prompt(q, common, args.plain)
        print(f"[{n:>2}/{len(todo)}] {q['id']} · {q['section']} · {q['topic']}", flush=True)
        collector = make_collector()
        started = datetime.now().astimezone().isoformat(timespec="seconds")
        t0 = time.perf_counter()
        try:
            response, context = await api.global_search(
                config=config,
                entities=tables["entities"],
                communities=tables["communities"],
                community_reports=tables["community_reports"],
                community_level=args.level,
                dynamic_community_selection=args.dynamic,
                response_type=args.response_type,
                query=prompt,
                callbacks=[collector],
                verbose=False,
            )
        except Exception as e:  # noqa: BLE001 - 한 문항의 실패가 전체를 막지 않게 한다
            consecutive_errors += 1
            err = {"id": q["id"], "error": f"{type(e).__name__}: {e}", "traceback": traceback.format_exc(), "prompt": prompt}
            write_json(out_dir / "records" / f"{q['id']}.error.json", err)
            print(f"        ✗ 오류: {type(e).__name__}: {e}", flush=True)
            if consecutive_errors >= args.max_errors:
                print(f"연속 오류 {consecutive_errors}회로 중단한다. 같은 --out으로 다시 실행하면 이어서 한다.", flush=True)
                return
            continue
        consecutive_errors = 0

        rec = build_record(q, prompt, response, context, collector, time.perf_counter() - t0, started, settings, args.usd_per_mtok)
        write_json(out_dir / "records" / f"{q['id']}.json", rec)
        (out_dir / "records" / f"{q['id']}.error.json").unlink(missing_ok=True)
        finalize_cb()

        c, u = rec["context"], rec["usage_estimate"]
        print(f"        → {STATUS_KO[rec['status']]} | 보고서 {c['n_reports']:,}개 · 묶음 {c['n_batches']}개 · 핵심 문장 {c['n_key_points']}개"
              f" | {rec['seconds']:.0f}초 | 입력≈{u['prompt_tokens'] / 1e6:.2f}M 토큰 ≈ ${u['cost_usd']:.2f}(캐시 미반영)", flush=True)
        for w in rec["warnings"]:
            print(f"        ⚠ {w}", flush=True)


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="평가 질문을 graphrag global 검색으로 일괄 실행하고 응답 기록을 파일로 남긴다.")
    ap.add_argument("--questions", default=str(HERE / "docs" / "questions_b_2001.md"), help="질문 문서")
    ap.add_argument("--answers", default=str(HERE / "docs" / "questions_b_2001_evidence.md"),
                    help="정답 문서. answers.md에 붙이는 용도이며 모델에는 보내지 않는다")
    ap.add_argument("--root", default=str(HERE / "enron"), help="graphrag 프로젝트 폴더")
    ap.add_argument("--data", help="다른 구축 결과 폴더(parquet이 있는 곳). 예: previous_builds/3_first_half_3661mails/output")
    ap.add_argument("--level", type=int, default=2, help="읽을 커뮤니티 층. 기본 2. 0은 80개만 읽어 싸고 빠르다")
    ap.add_argument("--dynamic", action="store_true", help="동적 커뮤니티 선택을 켠다. 선택 단계의 호출은 토큰 추정에 들어가지 않는다")
    ap.add_argument("--response-type", default="Multiple Paragraphs", help="graphrag query의 --response-type과 같다")
    ap.add_argument("--only", nargs="+", metavar="Q", help="일부만 실행. 예: Q03 Q05 또는 Q01-Q10")
    ap.add_argument("--plain", action="store_true", help="지시문 없이 질문만 보낸다")
    ap.add_argument("--out", help="결과 폴더. 기본은 results/<시각>_L<층>. 기존 폴더를 주면 이어서 실행한다")
    ap.add_argument("--force", action="store_true", help="이미 끝난 문항도 다시 돌린다 (돈이 든다)")
    ap.add_argument("--dry-run", action="store_true", help="API를 부르지 않고 계획만 출력한다")
    ap.add_argument("--max-errors", type=int, default=3, help="연속 오류가 이 횟수가 되면 중단한다 (기본 3)")
    ap.add_argument("--usd-per-mtok", type=float, default=DEFAULT_USD_PER_MTOK,
                    help=f"비용 추정용 100만 토큰당 단가(달러). 기본 {DEFAULT_USD_PER_MTOK}는 캐시가 없을 때의 단독 실행 단가라 연속 실행의 실제 비용보다 높다")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    for stream in (sys.stdout, sys.stderr):  # 윈도우 콘솔(cp949)에서 한글·특수 따옴표 출력 오류를 막는다
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass

    # load_config가 작업 폴더를 바꾸므로, 상대 경로는 그 전에 모두 절대 경로로 바꿔 둔다.
    root = Path(args.root).resolve()
    data = Path(args.data).resolve() if args.data else None
    out_dir = Path(args.out).resolve() if args.out else HERE / "results" / f"{datetime.now():%Y%m%d-%H%M%S}_L{args.level}"
    questions_path, answers_path = Path(args.questions).resolve(), Path(args.answers).resolve()

    common, questions = parse_questions(questions_path)
    if not questions:
        sys.exit(f"질문을 찾지 못했다: {questions_path}")
    selected = select_questions(questions, args.only)
    key = parse_answer_key(answers_path)

    try:
        config, tables = load_graph(root, data)
    except Exception as e:  # noqa: BLE001
        sys.exit(f"graphrag 설정이나 인덱스를 읽지 못했다: {type(e).__name__}: {e}\n"
                 "enron/.env에 GRAPHRAG_API_KEY가 있는지, --root/--data 경로가 맞는지 확인한다.")

    import importlib.metadata as md
    mi = model_info(config)
    settings = {
        "community_level": args.level, "dynamic": args.dynamic, "response_type": args.response_type, "plain": args.plain,
        "data_dir": str(data) if data else None, "model": mi["model"], "call_args": mi["call_args"],
    }
    rep_index = {int(r.community): (int(r.level), str(r.title)) for r in tables["community_reports"].itertuples()}

    n_reports = None if args.dynamic else count_reports(tables, args.level)
    per_q_tokens = (n_reports or 0) * TOKENS_PER_REPORT
    per_q_cost = per_q_tokens / 1e6 * args.usd_per_mtok

    # 이어서 실행할 때, 이전 실행과 설정이 다르면 끝난 문항을 건너뛰는 것이 잘못이므로 가장 먼저 막는다.
    run_path = out_dir / "run.json"
    prev_run = json.loads(run_path.read_text(encoding="utf-8")) if run_path.exists() else None
    if prev_run and not args.force:
        keys = ("community_level", "dynamic", "response_type", "plain", "data_dir")
        diff = [k for k in keys if prev_run["settings"].get(k) != settings[k]]
        if diff:
            sys.exit(f"이 폴더의 이전 실행과 설정이 다르다 ({', '.join(diff)}). 새 --out 폴더를 쓰거나, 다시 돌릴 거면 --force.")

    done_ids = {p.stem for p in (out_dir / "records").glob("Q??.json")} if (out_dir / "records").exists() else set()
    todo = selected if args.force else [q for q in selected if q["id"] not in done_ids]

    print(f"질문 {len(selected)}개 선택 (정답표 {sum(q['id'] in key for q in selected)}개 연결) · 층 {args.level} · "
          f"{'질문만 전송' if args.plain else '지시문 포함'} · 모델 {mi['model']}")
    if n_reports is not None:
        print(f"읽는 보고서 {n_reports:,}개 → 질문당 입력 약 {per_q_tokens / 1e6:.1f}M 토큰, 약 ${per_q_cost:.2f} (캐시 없는 단가 기준 추정)")
        print(f"이번에 돌릴 문항 {len(todo)}개 → 최대 약 ${per_q_cost * len(todo):.2f} (이미 끝난 문항 {len(selected) - len(todo)}개 제외. "
              "연속으로 돌리면 캐시로 더 낮아진다. 2026-11-24의 2층 30문항은 실제 약 3.4달러였다)")
    print(f"결과 폴더: {out_dir}")

    if args.dry_run:
        print("\n── 드라이런: API를 부르지 않았다 ──")
        for q in selected:
            print(f"  {q['id']} · {q['section']:<6} · 프롬프트 {len(build_prompt(q, common, args.plain)):>4}자 · {q['topic']}")
        first = selected[0]
        print(f"\n{first['id']}에 실제로 보낼 프롬프트:\n{'-' * 60}\n{build_prompt(first, common, args.plain)}\n{'-' * 60}")
        return
    if not todo:
        print("돌릴 문항이 없다. 다시 돌리려면 --force.")
        return

    (out_dir / "records").mkdir(parents=True, exist_ok=True)
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    run = prev_run or {"created_at": now}
    run["settings"] = settings
    run.update({
        "graphrag_version": md.version("graphrag"),
        "n_selected": len(selected),
        "questions_file": str(questions_path),
        "usd_per_mtok": args.usd_per_mtok,
        "note": "토큰은 map 단계 호출의 추정치로 실제보다 몇 % 낮다(reduce 단계 제외). 비용은 이 토큰에 캐시 없는 단가를 곱한 값이라 "
                "프롬프트 캐시가 적용되면 실제는 더 낮다. 정확한 사용량은 실행이 끝날 때 enron/logs/query.log 끝에 남는 "
                "Metrics 블록(이번 실행 전체 합계)과 OpenAI 콘솔(cached 입력 토큰 포함)에서 본다.",
    })

    def finalize_cb() -> dict:
        return finalize(out_dir, run, key, rep_index)

    try:
        asyncio.run(run_all(args, config, tables, todo, common, out_dir, settings, finalize_cb))
    except KeyboardInterrupt:
        print("\n중단했다. 같은 --out으로 다시 실행하면 끝난 문항은 건너뛰고 이어서 한다.", flush=True)
    finally:
        totals = finalize_cb()

    print(f"\n완료 {totals['done']}/{len(selected)}문항 · 응답 {totals['answered']} · 답 없음 {totals['no_data']} · "
          f"추정 입력 {totals['est_prompt_tokens'] / 1e6:.2f}M 토큰 (캐시 없는 단가로 ≈ ${totals['est_cost_usd']:.2f}, 실제는 더 낮을 수 있다)")
    errs = sorted(p.name for p in (out_dir / "records").glob("Q??.error.json"))
    if errs:
        print(f"오류가 난 문항 {len(errs)}개: {', '.join(e.split('.')[0] for e in errs)} (records/*.error.json 참고)")
    print(f"기록: {out_dir / 'answers.md'}\n      {out_dir / 'summary.csv'}\n      {out_dir / 'records'}")
    print("정확한 사용량: 프로그램이 끝나면 enron/logs/query.log 끝에 이번 실행 전체의 Metrics 블록이 남는다. 금액과 cached 입력 토큰 수는 OpenAI 콘솔에서 확인.")


if __name__ == "__main__":
    main()
