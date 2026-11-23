# Enron

Enron 메일로 GraphRAG 지식그래프를 구축하고, 넓은 질문을 도중에 멈추는 방법을 실험하는 프로젝트다.
지금은 본 구축(메일 3,661통)까지 끝난 상태다.

## 문서

| 문서 | 내용 |
|---|---|
| [docs/data.md](docs/data.md) | 원본 데이터 구조와 전처리 단계 |
| [docs/trial_500.md](docs/trial_500.md) | 500통 시험 구축에서 정한 것과 결과 |
| [docs/scale_decision.md](docs/scale_decision.md) | 본 구축 규모를 정하기 위한 비용과 선택지 |
| [docs/main_build.md](docs/main_build.md) | 본 구축 결과, 요금 등급, 하반기를 추가할 때의 예상 |

## 받은 뒤 할 일

파이썬 3.12 기준이다.

1. 가상환경을 만들고 graphrag를 설치한다.

   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install graphrag==3.3.0
   ```

2. `enron/.env.example`을 복사해 `enron/.env`로 만들고 OpenAI API 키를 넣는다.

   ```
   GRAPHRAG_API_KEY=sk-...
   ```

3. 질문을 돌려 본다. 본 구축 결과(`enron/output`)가 저장소에 들어 있어 다시 구축하지 않아도 된다.

   ```
   graphrag query --root ./enron --method global "What were the main issues in this period?"
   ```

   질문 하나에 약 0.25달러로 예상한다. 본 구축 그래프에서 아직 재 보지 않았다.

## 폴더

| 폴더 | 내용 |
|---|---|
| `enron/` | **본 그래프** (메일 3,661통). 실험에는 이것만 쓴다 |
| `trial_500/` | 500통 사전 구축 테스트. 비교와 기록용이다 |
| `docs/` | 문서 |

## 직접 구축하려면

1. Kaggle의 "The Enron Email Dataset"에서 `emails.csv`를 받아 `emails.csv/emails.csv`에 둔다 (1.4GB).
2. 전처리한다.

   ```
   python preprocess.py --mailboxes dasovich-j kean-s shapiro-r steffes-j --start 2001-01-01 --end 2001-07-01
   ```

3. 구축한다. 3,661통에 약 11~12달러, 2시간 40분쯤 든다.

   ```
   graphrag index --root ./enron
   ```

## 주의

- `enron/.env`는 커밋하지 않는다. `.gitignore`에 들어 있다.
- 모델은 `gpt-6-luna`로 고정한다. 바꾸면 이전 결과와 비교할 수 없다.
- `enron/output`을 다시 구축하면 커뮤니티가 달라진다. 팀이 같은 결과를 쓰려면 저장소의 것을 그대로 쓴다.
- LLM 호출은 비용이 든다. OpenAI 콘솔에서 지출 한도를 걸어 둔다.
