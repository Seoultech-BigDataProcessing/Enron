"""Enron emails.csv 전처리: 파싱 -> 부분 추출 -> 인용문 제거 -> 잡음 제거 -> 중복 제거 -> CSV 저장.

예) python preprocess.py --mailboxes dasovich-j --start 2001-01-01 --limit 500
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from email import message_from_string
from email.utils import parsedate_to_datetime
from pathlib import Path

csv.field_size_limit(2**31 - 1)

# 이 줄부터 아래는 인용문/전달문/고지문으로 보고 잘라 낸다.
CUT = re.compile(
    r"^\s*-+\s*Original Message\s*-+"
    r"|^\s*-+\s*Forwarded by\b"
    r"|^.{0,80}\d{1,2}/\d{1,2}/\d{2,4} \d{1,2}:\d{2}(:\d{2})? ?[AP]M\s*$"  # Lotus Notes 인용 머리줄
    r"|^\s*This e-mail is the property of Enron"
    r"|^\s*\*{20,}",
    re.MULTILINE | re.IGNORECASE,
)
AUTO_SENDER = re.compile(
    r"no\.address|announcements|outlook\.team|mailer-daemon|postmaster|"
    r"enron\.general|office\.chairman|arsystem|perfmgmt|exchange\.administrator",
    re.IGNORECASE,
)
SKIP_FOLDERS = {"calendar", "schedule_crawler", "contacts", "tasks"}
MIN_BODY = 100  # 정리 후 본문이 이보다 짧으면 버린다 (글자 수)
MAX_BODY = 20000  # 이보다 길면 뉴스 모음/뉴스레터로 보고 버린다
MAX_TO = 5  # 본문 머리의 To 줄에 적는 수신자 수 상한


def clean_body(body: str) -> str:
    m = CUT.search(body)
    if m:
        # 잘린 지점 바로 위에 남는 들여쓴 줄(인용 머리줄의 이름 등)도 함께 지운다.
        body = re.sub(r"(\n[ \t]+\S[^\n]*)+\s*$", "", body[: m.start()])
    lines = [ln for ln in body.splitlines() if not ln.lstrip().startswith(">")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="emails.csv/emails.csv")
    ap.add_argument("--out", default="enron/input/emails.csv")
    ap.add_argument("--mailboxes", nargs="+", required=True, help="예: dasovich-j shapiro-r")
    ap.add_argument("--start", default="1999-01-01", help="YYYY-MM-DD (포함)")
    ap.add_argument("--end", default="2003-01-01", help="YYYY-MM-DD (제외)")
    ap.add_argument("--limit", type=int, help="기간 안에서 날짜순으로 앞에서 N통만")
    args = ap.parse_args()

    boxes = set(args.mailboxes)
    n = Counter()
    seen = set()
    rows = []

    with open(args.src, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            n["원본 전체"] += 1
            parts = row["file"].split("/")
            if parts[0] not in boxes:
                continue
            n["선택한 메일함"] += 1
            msg = message_from_string(row["message"])
            try:
                date = parsedate_to_datetime(msg["Date"]).strftime("%Y-%m-%d %H:%M")
            except (TypeError, ValueError):
                continue
            if not (args.start <= date[:10] < args.end):
                continue
            n["기간 안"] += 1
            sender = (msg["From"] or "").strip()
            if not sender.lower().endswith("@enron.com"):
                n["제외: 사외 발신 (뉴스레터, 광고, 메일링 리스트)"] += 1
                continue
            if (len(parts) > 2 and parts[1] in SKIP_FOLDERS) or AUTO_SENDER.search(sender):
                n["제외: 자동 발송/일정 폴더"] += 1
                continue
            raw = msg.get_payload(decode=True) or b""  # quoted-printable 해제
            body = clean_body(raw.decode(msg.get_content_charset() or "utf-8", "replace"))
            if len(body) < MIN_BODY:
                n["제외: 본문 짧음"] += 1
                continue
            if len(body) > MAX_BODY:
                n["제외: 본문 김"] += 1
                continue
            subject = " ".join((msg["Subject"] or "").split())
            key = hashlib.md5("\x00".join([sender, date, subject, body]).encode("utf-8", "replace")).digest()
            if key in seen:
                n["제외: 중복"] += 1
                continue
            seen.add(key)
            to = " ".join(", ".join(filter(None, [msg["To"], msg["Cc"]])).split())
            rows.append((date, subject, sender, to, body))

    rows.sort()
    n["정리 후"] = len(rows)
    if args.limit:
        rows = rows[: args.limit]
    n["저장"] = len(rows)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["title", "sender", "recipients", "date", "text"])
        for date, subject, sender, to, body in rows:
            # 단체 메일의 수신자 명단이 그래프를 채우지 않도록 본문에는 앞 5명만 적는다.
            names = to.split(", ")
            short = ", ".join(names[:MAX_TO]) + (f" and {len(names) - MAX_TO} others" if len(names) > MAX_TO else "")
            head = f"From: {sender}\nTo: {short}\nDate: {date}\nSubject: {subject}\n\n"
            w.writerow([subject or "(no subject)", sender, to, date, head + body])

    stats = {
        "args": vars(args),
        "counts": dict(n),
        "date_range": [rows[0][0], rows[-1][0]] if rows else None,
        "text_chars": sum(len(r[4]) for r in rows),
    }
    out.with_name("preprocess_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
