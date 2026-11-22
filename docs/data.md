# Enron 메일 데이터와 전처리

원본 `emails.csv/emails.csv`(1.4GB, 517,401행)의 구조와, `preprocess.py`가 하는 일을 정리한다.
숫자는 모두 원본에서 직접 센 값이다.

## 1. 원본의 열

열은 두 개뿐이다.

| 열 | 내용 | 예 |
|---|---|---|
| `file` | 메일이 들어 있던 위치. `메일함/폴더/번호` 형식 | `dasovich-j/all_documents/8149.` |
| `message` | 메일 원문 전체. 헤더와 본문이 한 문자열로 합쳐져 있다 | 2절 참고 |

### `file` 열 읽는 법

`dasovich-j/all_documents/8149.` 을 `/`로 나누면 세 부분이다.

- **메일함** `dasovich-j`: 이 메일을 가지고 있던 직원이다. `성-이름 첫 글자` 형식이라 `dasovich-j`는 Jeff Dasovich의 메일함이다. 전체 150개가 있다.
- **폴더** `all_documents`: 그 직원의 메일 프로그램 안 폴더다. `inbox`, `sent`, `deleted_items` 등이 있다.
- **번호** `8149.`: 폴더 안에서의 순번이다. 의미는 없다.

메일함은 "그 사람이 보낸 메일"이 아니라 "그 사람의 메일 프로그램에 있던 메일 전부"다.
받은 메일, 보낸 메일, 참조로 받은 메일이 모두 들어 있다.

### 시험 구축과 본 구축 후보 메일함

| 메일함 | 주인 | 원본 행 수 |
|---|---|---|
| `dasovich-j` | Jeff Dasovich | 28,234 |
| `kean-s` | Steven Kean | 25,351 |
| `shapiro-r` | Richard Shapiro | 6,071 |
| `steffes-j` | James Steffes | 3,331 |

네 사람은 엔론의 대관·규제 대응 부서 소속으로 알려져 있다(Dasovich는 캘리포니아 담당).
이 직책 정보는 데이터에 적혀 있지 않고 공개된 엔론 자료에서 온 배경 지식이다.
데이터로 확인한 것은, `dasovich-j`의 2001년 초 메일이 캘리포니아 전력 위기, 가격 상한, 주 의회 대응을 다룬다는 점이다.

같은 부서의 메일함을 고르는 이유는 같은 사건을 여러 사람이 주고받기 때문이다.
그래프에서 엔티티가 촘촘히 연결되고 커뮤니티가 주제별로 묶인다.
서로 무관한 메일함을 섞으면 그래프가 끊긴다.

## 2. 실제 데이터 예시

`file` = `dasovich-j/all_documents/8149.` 인 행의 `message` 값이다.
참조 목록이 70명 가까이 되어 가운데만 줄였고, 나머지는 원문 그대로다.

```
Message-ID: <23908078.1075843316923.JavaMail.evans@thyme>
Date: Thu, 4 Jan 2001 08:18:00 -0800 (PST)
From: vicki.sharp@enron.com
To: jeff.dasovich@enron.com, mike.smith@enron.com, wanda.curry@enron.com, 
	don.black@enron.com, marty.sunde@enron.com, 
	dennis.benevides@enron.com, scott.stoness@enron.com, 
	harry.kingerski@enron.com, kevin.hughes@enron.com, 
	william.bradford@enron.com
Subject: Re: Brief Summary of Today's Activities in California (at Least
 Thus Far)
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Vicki Sharp
X-To: Jeff Dasovich, Mike D Smith, Wanda Curry, Don Black, Marty Sunde, ...
X-cc: 
X-bcc: 
X-Folder: \Jeff_Dasovich_June2001\Notes Folders\All documents
X-Origin: DASOVICH-J
X-FileName: jdasovic.nsf

We just received a letter from the PX asking us to enter into an indemnity 
agreement with them or requiring us to post collateral for the full amount of 
the unsecured credit exposure.  We are researching this issue from the EES 
side.  Wanda and Don, we are sending this letter to you.  Can you determine 
what amounts we are talking about for EES?   This letter has also been sent 
to EPMI and Portland General and I assume will be reviewed by their legal 
team.  Bill Bradford, have you sent this on to Portland General.?
If I have missed someone that this memo should have been forwarded to, please 
forward it on. 
Jeff Dasovich, can you forward to Mike Day?


From: Jeff Dasovich@ENRON on 01/04/2001 02:58 PM
Sent by: Jeff Dasovich@ENRON
To: Jeff Dasovich/NA/Enron@Enron
cc: Alan Comnes/PDX/ECT@ECT, Angela Schwarz/HOU/EES@EES, Beverly 
Aden/HOU/EES@EES, Bill Votaw/HOU/EES@EES, ... (참조 약 70명, 줄임)
(이 아래로 Dasovich가 쓴 원래 메일 전문이 이어진다)
```

이 한 통에서 원본의 특징 네 가지를 볼 수 있다.

1. **헤더와 본문이 한 덩어리다.** 첫 빈 줄 위가 헤더, 아래가 본문이다. 보낸 사람, 날짜, 제목은 열이 아니라 헤더 줄에 있다.
2. **쓸모 있는 헤더는 일부다.** `From`, `To`, `Cc`, `Date`, `Subject`만 쓴다. `X-`로 시작하는 줄은 메일 프로그램이 붙인 정보다.
3. **본문 뒤에 이전 메일이 통째로 붙어 있다.** `From: Jeff Dasovich@ENRON on 01/04/2001 02:58 PM` 줄부터는 Vicki Sharp가 쓴 글이 아니라 답장 대상인 원래 메일이다. 그 원래 메일은 데이터에 별도 행으로도 들어 있다.
4. **같은 메일이 여러 번 나온다.** 이 메일은 받는 사람이 10명이라, 그중 메일함이 데이터에 포함된 사람마다 한 번씩 들어 있을 수 있다. 한 사람의 메일함 안에서도 `all_documents` 같은 폴더에 같은 메일이 다시 들어 있는 경우가 많다.

## 3. 원본 전체의 규모

| 항목 | 값 |
|---|---|
| 전체 행 | 517,401 |
| 내용이 같은 메일을 하나로 쳤을 때 | 255,170 (약 절반이 중복) |
| 메일함 수 | 150 |
| 메일이 몰린 기간 | 2000년 ~ 2002년 초, 최다는 2001년 10~11월 |
| 본문 길이 중앙값 | 765자 |
| 본문 길이 상위 10% | 3,736자 이상 |

폴더별로는 `all_documents`(128,103), `discussion_threads`(58,609), `sent`(57,653), `deleted_items`(51,356), `inbox`(44,859) 순으로 많다.
`all_documents`와 `discussion_threads`는 다른 폴더의 메일을 다시 담고 있어 중복의 주된 원인이다.

## 4. 전처리 순서와 이유

`preprocess.py`는 아래 순서로 처리한다. 앞 단계일수록 계산이 싸고 많이 걸러 낸다.

| 순서 | 하는 일 | 이유 |
|---|---|---|
| 1 | **메일함 선택.** `file`의 첫 부분이 지정한 메일함인 행만 남긴다 | 전체 25만 통을 LLM에 넣으면 비용이 감당되지 않는다. 무작위로 뽑으면 대화가 끊겨 그래프가 듬성듬성해지므로 메일함 단위로 통째로 고른다 |
| 2 | **헤더 파싱.** `message`에서 보낸 사람, 받는 사람, 참조, 날짜, 제목, 본문을 분리한다 | 이후 모든 단계가 이 값들을 쓴다 |
| 3 | **기간 선택.** 날짜가 지정 범위 안인 메일만 남긴다 | 연속된 기간을 통째로 잘라야 한 사건의 흐름이 유지된다 |
| 4 | **사외 발신 제외.** 보낸 사람이 `@enron.com`이 아니면 뺀다 | 광고, 뉴스레터, 메일링 리스트가 많다(아마존 광고, MBA 과정 공지, 통신 업계 소식지). 업무 내용이 아니고 그래프에 무관한 엔티티를 만든다 |
| 5 | **자동 발송과 일정 폴더 제외.** 전사 공지 계정, 시스템 알림, `calendar` 폴더 등을 뺀다 | 사람이 쓴 업무 대화가 아니다 |
| 6 | **인코딩 해제.** 본문의 `=20`, `=09` 같은 기호를 원래 글자로 되돌린다 | 일부 메일이 quoted-printable 방식으로 저장되어 있어, 그대로 두면 단어가 깨진다 |
| 7 | **인용문, 전달문, 고지문 잘라 내기.** 아래 표시가 나오는 줄부터 끝까지 버린다 | 2절 예시처럼 이전 메일이 통째로 붙어 있다. 안 지우면 같은 내용이 답장마다 반복되어, 프로젝트가 재려는 "반복"이 데이터 탓으로 부풀려진다 |
| 8 | **너무 짧거나 긴 본문 제외.** 100자 미만, 2만 자 초과를 뺀다 | 짧은 것은 "Thanks" 수준이라 정보가 없다. 긴 것은 기사 모음이나 소식지라 업무 대화가 아니고 LLM 비용만 크다 |
| 9 | **중복 제거.** (보낸 사람, 날짜, 제목, 정리된 본문)이 같으면 하나만 남긴다 | 같은 메일이 여러 폴더와 여러 메일함에 들어 있다. 7단계 뒤에 해야 인용문 차이만 있는 사본도 걸러진다 |
| 10 | **날짜순 정렬 후 앞에서 N통.** `--limit`을 준 경우에만 | 시험 구축용. 날짜순으로 앞에서 자르면 연속된 기간이 된다 |
| 11 | **저장.** 본문 앞에 보낸 사람, 받는 사람, 날짜, 제목을 붙여 CSV로 쓴다. 받는 사람은 앞 5명만 적고 나머지는 `and N others`로 줄인다 | GraphRAG는 본문 텍스트만 읽는다. 사람 정보를 본문에 넣어야 "누가 누구에게"가 그래프에 잡힌다. 명단을 전부 적었던 첫 시험 구축에서는 관계의 약 40%가 "메일을 받았다"였고, 내용 없는 수신자 명단 보고서가 생겼다 |

7단계에서 자르는 표시는 다음과 같다.

| 표시 | 뜻 |
|---|---|
| `-----Original Message-----` | Outlook 방식의 답장 인용 |
| `From: 이름 on 01/04/2001 02:58 PM` 처럼 날짜와 시각으로 끝나는 줄 | Lotus Notes 방식의 답장 인용 (2절 예시) |
| `---- Forwarded by ...` | 전달된 메일 |
| `This e-mail is the property of Enron ...`, `*` 20개 이상 | 법적 고지문 |
| `>` 로 시작하는 줄 | 줄 단위 인용 (그 줄만 삭제) |

### 하지 않는 것

- **서명 제거.** 서명 형태가 사람마다 달라 규칙으로 지우면 본문까지 잘릴 수 있다. 시험 구축에서 서명이 엔티티로 잡히는지 보고 결정한다.
- **사외 업무 메일 살리기.** 4단계에서 업계 단체가 보낸 업무 메일도 함께 빠진다. 광고와 구분할 간단한 기준이 없어 전부 뺐다.

## 5. 결과물

`enron/input/emails.csv`에 저장된다.

| 열 | 내용 |
|---|---|
| `title` | 제목 |
| `sender` | 보낸 사람 |
| `recipients` | 받는 사람과 참조 |
| `date` | `YYYY-MM-DD HH:MM` (원문에 적힌 현지 시각 그대로) |
| `text` | 머리 네 줄(From, To, Date, Subject) + 정리된 본문. GraphRAG가 읽는 열 |

2절의 예시는 처리 후 `text`가 이렇게 된다.

```
From: vicki.sharp@enron.com
To: jeff.dasovich@enron.com, mike.smith@enron.com, wanda.curry@enron.com, don.black@enron.com, marty.sunde@enron.com and 5 others
Date: 2001-01-04 08:18
Subject: Re: Brief Summary of Today's Activities in California (at Least Thus Far)

We just received a letter from the PX asking us to enter into an indemnity 
agreement with them or requiring us to post collateral for the full amount of 
(중략)
forward it on. 
Jeff Dasovich, can you forward to Mike Day?
```

단계별 건수는 실행할 때마다 `enron/input/preprocess_stats.json`에 기록된다.
`dasovich-j`, 2001-01-01 이후, 500통으로 실행한 결과는 다음과 같다.

| 단계 | 건수 |
|---|---|
| 메일함 전체 | 28,234 |
| 기간 안 | 18,363 |
| 사외 발신 제외 | −5,227 |
| 자동 발송·일정 폴더 제외 | −76 |
| 본문 100자 미만 제외 | −5,224 |
| 본문 2만 자 초과 제외 | −507 |
| 중복 제외 | −2,985 |
| 남은 것 | 4,344 |
| 저장 (앞에서 500통, 2001-01-01 ~ 02-20) | 500 |

실행 방법:

```
python preprocess.py --mailboxes dasovich-j --start 2001-01-01 --limit 500
```
