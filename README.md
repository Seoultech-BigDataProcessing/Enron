# Enron

Enron 메일로 GraphRAG 지식그래프를 구축하고, 넓은 질문을 도중에 멈추는 방법을 실험하는 프로젝트다.
지금은 본 구축(2001년 1년치 메일 8,431통)까지 끝난 상태다.

## 문서

| 문서 | 내용 |
|---|---|
| [docs/data.md](docs/data.md) | 원본 데이터 구조와 전처리 단계 |
| [docs/trial_500.md](docs/trial_500.md) | 500통 시험 구축에서 정한 것과 결과 |
| [docs/scale_decision.md](docs/scale_decision.md) | 본 구축 규모를 정하기 위한 비용과 선택지 |
| [docs/main_build.md](docs/main_build.md) | 본 구축 결과와 품질, 요금 등급, 질문 비용 예상 |
| [docs/question_run_2001.md](docs/question_run_2001.md) | 질문 30개를 2층으로 돌린 결과 (비용, 응답 분류, 답이 없는 이유) |

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

   질문 하나(2층까지)에 약 0.1 ~ 0.4달러가 든다. 단독으로 돌리면 약 0.37달러, 30문항을 연속으로 돌리면 평균 약 0.11달러였다. 잰 결과는 [docs/question_run_2001.md](docs/question_run_2001.md)에 있다.

## 폴더

| 폴더 | 내용 |
|---|---|
| `enron/` | **본 그래프** (2001년 1년치, 메일 8,431통). 실험에는 이것만 쓴다 |
| `previous_builds/` | 이전 구축 (500통 사전 테스트 두 번, 상반기 3,661통). 기록용이다. 폴더 안 README에 설명이 있다 |
| `docs/` | 문서 |

## 직접 구축하려면

1. Kaggle의 "The Enron Email Dataset"에서 `emails.csv`를 받아 `emails.csv/emails.csv`에 둔다 (1.4GB).
2. 전처리한다.

   ```
   python preprocess.py --mailboxes dasovich-j kean-s shapiro-r steffes-j --start 2001-01-01 --end 2002-01-01
   ```

3. 구축한다. 8,431통을 처음부터 구축하면 약 25달러, 6시간쯤으로 예상한다.

   ```
   graphrag index --root ./enron
   ```

## 주의

- `enron/.env`는 커밋하지 않는다. `.gitignore`에 들어 있다.
- 모델은 `gpt-6-luna`로 고정한다. 바꾸면 이전 결과와 비교할 수 없다.
- `enron/output`을 다시 구축하면 커뮤니티가 달라진다. 팀이 같은 결과를 쓰려면 저장소의 것을 그대로 쓴다.
- LLM 호출은 비용이 든다. OpenAI 콘솔에서 지출 한도를 걸어 둔다.
