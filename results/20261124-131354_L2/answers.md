# 질문 응답 기록

- 실행: 2026-11-24T13:13:55+09:00 (갱신 2026-11-24T13:46:00+09:00)
- 설정: 층 2 · 동적 선택 끔 · 응답 형식 Multiple Paragraphs · 공통 지시문 + 유형별 지시문 + 질문 전송 · 모델 gpt-6-luna
- 진행: 30 / 30문항 기록 (응답 27, 답 없음 3)
- 추정 사용량: 입력 102,865,410 · 출력 1,861,605 토큰 ≈ $11.31 (map 단계 기준 추정. 정확한 금액은 OpenAI 콘솔)
- 응답의 `[Data: Reports (n)]`에서 n은 커뮤니티 보고서 번호다 (community_reports.parquet의 community 열).

| ID | 주제 | 상태 | 인용 보고서 수 |
|---|---|---|---|
| Q01 | 발전 프로젝트의 설비용량 | 응답 | 5 |
| Q02 | 시장별 거래 미성사 건수 | 답 없음(정형 문장) | 0 |
| Q03 | 캘리포니아 전력 환급 논의 금액 | 응답 | 11 |
| Q04 | 캘리포니아 천연가스 수송 계획 | 응답 | 9 |
| Q05 | 캘리포니아 전력 부족 전망 | 응답 | 1 |
| Q06 | 캘리포니아 발전소 건설 인센티브 | 답 없음(정형 문장) | 0 |
| Q07 | 다볼 발전회사 지분 | 응답 | 7 |
| Q08 | 미국 지역 송전기구의 최대부하 | 응답 | 1 |
| Q09 | 텍사스 전력시장 합병 검토 | 응답 | 4 |
| Q10 | 과거 순이익 재작성 | 답 없음(정형 문장) | 0 |
| Q11 | 직접구매 중단 기준일 | 응답 | 3 |
| Q12 | DWR 장기계약 비용 | 응답 | 9 |
| Q13 | PG&E 채권 신고와 재편안 | 응답 | 5 |
| Q14 | 미 동남부 송전기구 조정 | 응답 | 14 |
| Q15 | 9월 출장 직원 귀가 지원 | 응답 | 1 |
| Q16 | 미국 발전소 다중오염물질 규제안 | 응답 | 3 |
| Q17 | 다이너지 합병 발표의 투자 계획 | 응답 | 6 |
| Q18 | 거래상대방 담보 | 응답 | 6 |
| Q19 | 12월 추가 파산 신청 법인 | 응답 | 1 |
| Q20 | 다볼 미지급금과 지급보증 | 응답 | 9 |
| Q21 | 직접구매 중단과 기존 계약 검증 | 응답 | 11 |
| Q22 | DWR 계약 비용과 소비자 요금 | 응답 | 14 |
| Q23 | PG&E 파산 절차와 사업 분리 | 응답 | 6 |
| Q24 | 캘리포니아 도매전력 환급 절차 | 응답 | 9 |
| Q25 | 미 동북부 지역 송전기구 통합 | 응답 | 9 |
| Q26 | SEC 조사 대응과 정보 공개 | 응답 | 11 |
| Q27 | 퇴직급여 검토와 인력 감축 후 지원 | 응답 | 6 |
| Q28 | NEPOOL 재무보증과 선납 협상 | 응답 | 3 |
| Q29 | 교토의정서 이행과 배출권거래 | 응답 | 6 |
| Q30 | 다볼 발전사업 협상 | 응답 | 7 |

## Q01 · 발전 프로젝트의 설비용량

*상위 몇 개 · 응답 · 47초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 7개*

**질문**

> 10월 Project Phoenix 발전사업 검토와 같은 달 거래 심사(underwriters) 회의에 나온 신규 거래 요약들을 비교할 때, 설비용량이 가장 큰 발전사업 세 곳은 어디인가? 사업명과 MW를 적고 동률을 표시하라.

**응답**

> **확인 불가.** 제공된 보고서만으로는 10월 Project Phoenix 검토와 같은 달 underwriters 회의의 신규 거래 요약에 함께 포함된 발전사업을 확정할 수 없어, 해당 사업들 중 용량 상위 세 곳의 순위나 동률을 판정할 수 없습니다. 2001년 10월 26일 회의의 신규 거래로 확인되는 Columbia deal은 290 MW이지만, 이 정보만으로 요청한 발전사업 세 곳을 비교할 수는 없습니다 [Data: Reports (907)].
>
> 별도 보고서에는 FPL/Kelley 1,080 MW, NRG/Gila Bend 800 MW, FPL/Anderson 540 MW가 기재되어 있습니다. 그러나 이들이 모두 질문에서 지정한 비교 대상에 속한다는 근거는 없습니다 [Data: Reports (734, 4010, 4009)]. 또 Allegheny/La Paz는 1,080 MW로 언급되지만, 해당 회의의 지정된 신규 거래 요약에 포함됐는지는 확인되지 않습니다 [Data: Reports (3926)]. 따라서 이 수치들로 상위 세 곳이나 동률을 확정할 수 없습니다.

**응답이 인용한 보고서**

- 907 · L2 · Columbia Deal, Jake Thomas, and Tariff Discussions
- 734 · L1 · NRG, FPL, and Regional Power Projects
- 4010 · L2 · South Carolina and the FPL/Anderson Plant
- 4009 · L2 · NRG and the Gila Bend Generation Projects
- 3926 · L2 · Steve Montovano and Enron’s Eastern Seaboard Operations

**정답 (채점 기준)**

> FPL/Kelley와 Allegheny/La Paz가 각각 1,080 MW로 공동 1위이고, NRG/Gila Bend가 800 MW로 3위다. 다음은 FPL/Anderson 540 MW와 Columbia 290 MW다. 각 값은 사업 검토에 쓰인 설비 규모다.

원문 근거 번호(연간 CSV): 6448, 6597, 7036

## Q02 · 시장별 거래 미성사 건수

*상위 몇 개 · 답 없음(정형 문장) · 39초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 0개*

**질문**

> 10월 19일과 11월 19일에 공유된 시장별 거래 요약을 비교하라. 텍사스·뉴욕·매사추세츠·일리노이 가운데 각 보고 시점의 직전 한 달간 미성사 거래(lost deals) 건수가 가장 많이 늘어난 세 시장은 어디인가? 두 건수와 증감을 적어라.

**응답**

> I am sorry but I am unable to answer this question given the provided data.

**정답 (채점 기준)**

> 매사추세츠 40건 → 97건(+57), 일리노이 7건 → 48건(+41), 텍사스 13건 → 37건(+24) 순이다. 뉴욕은 10건 → 4건(−6)이다. 각 메일의 최근 한 달 또는 30일 집계를 비교한다.

원문 근거 번호(연간 CSV): 6522, 7770

## Q03 · 캘리포니아 전력 환급 논의 금액

*상위 몇 개 · 응답 · 64초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 60개*

**질문**

> 7월 CAISO의 캘리포니아 전력 환급 추정 하향 보도에서 주정부 주장, CAISO가 FERC에 제출한 수정 추정, FERC 행정판사 전망, 전력공급자 합의 제안의 금액을 비교하라. 금액이 큰 세 항목의 주체·금액·성격을 밝혀라.

**응답**

> 제공된 보고서로는 네 항목의 금액을 같은 기준으로 비교해 상위 세 항목을 확정할 수 없습니다. 주정부 주장액으로는 약 **89억 달러(거의 90억 달러)**가 확인되지만, 이 수치는 주정부의 환급 요구이지 확정된 과다 청구액이나 실제 환급액은 아닙니다. 보고서만으로는 이 주장이 질문에서 말한 7월 보도에 나온 주장과 동일한지 확인할 수 없습니다. [Data: Reports (382, 1746, 1835, 1635, 3120, +more)]
>
> 전력공급자들의 합의 제안액으로는 **7억 1,610만 달러**가 확인됩니다. 이는 합의 제안이지 수락·지급된 금액은 아니며, 관련 보고서에 따르면 협상은 2001년 7월 9일 합의 없이 끝났습니다. [Data: Reports (382, 1746, 2401, 79, 1496, +more)]
>
> **CAISO가 FERC에 제출한 수정 추정액과 FERC 행정판사의 전망액은 확인 불가**입니다. 따라서 확인 가능한 두 금액만 비교하면 주정부 요구액이 전력공급자 제안액보다 크지만, 누락된 두 수치가 있어 요청한 상위 세 항목의 주체·금액·성격을 순위로 제시할 수는 없습니다. [Data: Reports (1746, 1635, 2401, 1753, 382, +more)]
>
> 참고로 보고서에 언급된 CAISO의 62억 달러 수치는 경쟁시장 예상가격을 웃돈 규모에 관한 추정이며, 환급액 추정치로 제시된 것이 아니므로 위 비교에 포함할 수 없습니다. [Data: Reports (237, 1403)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 382 · L1 · California Power Refunds and FERC Market Proceedings
- 1746 · L2 · Gray Davis and California’s Electricity Crisis
- 1835 · L2 · Jim Brulte, California Meetings, and Davis Testimony
- 1635 · L2 · California Power-Market Refunds and Federal Oversight
- 3120 · L2 · U.S. Congress and Federal Energy Policy
- 2401 · L2 · California Power Refund Settlement Talks
- 79 · L0 · California Generator Refund Hearings
- 1496 · L2 · Edison, SB 78, and Supplier Disputes
- 1753 · L2 · California Power Refund and PG&E Negotiations
- 237 · L1 · California ISO, Enron, and the California Power-Market Crisis
- 1403 · L2 · ISO, Enron, and California Electricity-Market Oversight

**정답 (채점 기준)**

> 캘리포니아 주정부 주장 89억 달러 → CAISO가 FERC에 제출한 수정 추정 61억 달러 → 커티스 와그너 행정판사의 전망 약 10억 달러 순이다. 전력공급자 합의 제안은 7억 달러를 조금 넘었다. 보도에 함께 나온 77억 달러는 다른 가격 기준을 적용했을 때의 추산이다.

원문 근거 번호(연간 CSV): 4233

## Q04 · 캘리포니아 천연가스 수송 계획

*상위 몇 개 · 응답 · 72초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 64개*

**질문**

> 3월 말 엔론이 지지한 Kern River·El Paso 긴급 증설안과 6월 Kramer Junction 보도에 제시된 증설 용량 또는 확정 인도 용량을 비교하라. 큰 세 항목을 일일 백만 입방피트(MMcf/d)로 환산하고 시설별로 어떤 계획인지 적어라.

**응답**

> ### 결론
>
> 요청한 세 항목을 동일한 기준으로 확정해 순위화하기는 **확인 불가**입니다. 제공된 보고서들은 3월 말 엔론이 지지한 Kern River·El Paso 긴급 증설안의 용량을 확인해 주지 않고, 6월 Kramer Junction 보도의 날짜와 해당 보도에 실린 수치를 명확히 연결하지도 않습니다. 따라서 관련 자료에 등장하는 수치들을 요청한 계획의 용량으로 단정할 수 없습니다. [Data: Reports (1127, 1516, 3204, 3172, +more)]
>
> 참고로, Kramer Junction 관련 보고서에는 미터 스테이션의 **최대 500 MMcf/d 1차 확정 인도 용량 제안**과 별도의 신규 인입점 **200 MMcf/d 제안 용량**이 나옵니다. 둘 다 제안 수치이며, 실제 확정·가동 용량으로 확인되지는 않습니다. 이 두 항목은 서로 다른 시설·제안이므로 합산할 수 없습니다. [Data: Reports (519, 3172)]
>
> 그 밖에 Kern River의 California Action Project에는 **135 MMcf/d** 추가 수송 계획이 기재되어 있습니다. 그러나 이 계획이 질문의 3월 말 긴급 증설안이라는 근거는 없습니다. El Paso 남부 시스템의 **약 230 MMcf/d** 증설 계획도 보고되어 있지만, 이를 엔론이 지지한 해당 긴급 증설안과 동일시할 근거는 없습니다. [Data: Reports (3161, 3173, 3198, 3204)]
>
> 따라서 위 수치들은 관련 보고서에서 확인되는 참고값일 뿐, 질문에서 지정한 자료의 큰 세 항목으로 순위를 매길 수는 없습니다. Kramer Junction의 ENA 배정량 약 3,700 Dth/d도 보고되어 있으나, 이를 MMcf/d로 환산할 기준이 제공되지 않아 비교값으로 확정하기 어렵습니다. [Data: Reports (517, 3161)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 1127 · L2 · Enron Correspondents in California Energy Proceedings
- 1516 · L2 · SoCal Gas and California Gas Infrastructure
- 3204 · L2 · El Paso Expansion Proposal and Summer System Testing
- 3172 · L2 · Kern River Gas Transmission Expansion Network
- 519 · L1 · Kern River, Wheeler Ridge, and California Gas Expansion
- 3161 · L2 · Kern River Pipeline Expansion and SoCal Gas Rights
- 3173 · L2 · Wheeler Ridge, Kern River, and SoCalGas
- 3198 · L2 · El Paso and California Gas Market Proceedings
- 517 · L1 · Kern River Pipeline Expansions and Capacity Rights

**정답 (채점 기준)**

> ① Kern River의 Kramer Junction 계량소 제안은 최대 500 MMcf/d의 확정 인도 용량이다. ② El Paso 남부계통은 기존 압축기 유지 시 230,000 Mcf/d(230 MMcf/d)의 추가 용량이다. ③ SoCalGas의 Kramer Junction 계통 증설 계획은 200 MMcf/d다. Kern River의 3월 임시 압축기 증설안은 135 MMcf/d다. 두 Kramer Junction 수치는 별개 사업의 표기 용량이다.

원문 근거 번호(연간 CSV): 1499, 3335

## Q05 · 캘리포니아 전력 부족 전망

*상위 몇 개 · 응답 · 44초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 1개*

**질문**

> 2월 말 보도에 인용된 캘리포니아 계통운영기관의 5~8월 전망에서 전력 부족량이 가장 큰 세 달은 언제인가? 기본 전망을 기준으로 각 달의 부족량을 MW로 적어라.

**응답**

> 확인 불가. 제공된 보고서에는 2월 말 보도에 인용된 캘리포니아 계통운영기관의 5~8월 기본 전망치와 월별 전력 부족량(MW)이 없어, 부족량이 가장 큰 세 달과 각 수치를 비교할 수 없습니다. [Data: Reports (146)]

**응답이 인용한 보고서**

- 146 · L1 · SF Gate, Enron Deregulation, and California Power

**정답 (채점 기준)**

> 6월 6,815 MW → 8월 5,297 MW → 7월 4,685 MW. 나머지는 5월 3,030 MW다. 기사에 인용된 당시 전망치다.

원문 근거 번호(연간 CSV): 933

## Q06 · 캘리포니아 발전소 건설 인센티브

*상위 몇 개 · 답 없음(정형 문장) · 71초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 0개*

**질문**

> 캘리포니아 행정명령 D-32-01의 발전소 건설 인센티브를 가동 개시일과 평균 출력 구간별로 비교하라. 여섯 조합 중 MW당 지급 단가가 가장 높은 세 조합과 금액은 무엇인가?

**응답**

> I am sorry but I am unable to answer this question given the provided data.

**정답 (채점 기준)**

> 모두 평균 출력의 최초 100 MW분이다. ① 7월 1일까지 가동 시 $5,000/MW ② 7월 2일~8월 1일 $4,000/MW ③ 8월 2~31일 $3,000/MW. 같은 세 기간의 100 MW 초과분은 각각 $2,500, $2,000, $1,500/MW다.

원문 근거 번호(연간 CSV): 2224

## Q07 · 다볼 발전회사 지분

*상위 몇 개 · 응답 · 71초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 24개*

**질문**

> 9월과 11월에 공유된 다볼 발전회사 관련 보도에 나타난 지분 구조에서 지분율이 가장 높은 주주 두 곳은 어디인가? 지분율과 함께 큰 순서대로 적어라.

**응답**

> 제공된 자료에서 확인되는 지분율을 기준으로 하면 **Enron(65%)**이 가장 높고, 그다음은 **Maharashtra State Electricity Board(MSEB, 15%)**입니다. [Data: Reports (419, 2696, 2677, 418)]
>
> 다만 이 지분 구조가 질문에서 지정한 9월·11월 공유 보도 각각에 실린 것인지, 또는 두 보도에서 같은 기준으로 제시된 것인지는 확인할 수 없습니다. 따라서 **해당 보도에 한정한 순위는 확인 불가**입니다. [Data: Reports (2670, 3019, 2636)]

**응답이 인용한 보고서**

- 419 · L1 · Enron–Dabhol Project and Maharashtra Payment Dispute
- 2696 · L2 · Enron, Dabhol, and India’s Power-Sector Dispute
- 2677 · L2 · Dabhol Power Company, Enron, and the MSEB Dispute
- 418 · L1 · Dabhol Power Project: Enron, DPC, and MSEB
- 2670 · L2 · MSEB–Dabhol Power Dispute and Renegotiations
- 3019 · L2 · Bush–Indian Prime Minister Meeting on Dabhol
- 2636 · L2 · Dabhol Power Dispute and Indian Government

**정답 (채점 기준)**

> 엔론이 65%로 1위, Maharashtra State Electricity Board(MSEB)가 15%로 2위다. General Electric과 Bechtel은 각각 10%로 순위 밖이다. 두 시기의 보도에 같은 지분 구조가 나온다.

원문 근거 번호(연간 CSV): 5592, 7727

## Q08 · 미국 지역 송전기구의 최대부하

*상위 몇 개 · 응답 · 42초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 1개*

**질문**

> 10월 바턴의 지역 송전기구(RTO) 규모 기준을 검토할 때 작성한 최대부하 목록과 보충 목록을 비교하라. 값이 큰 세 권역과 각각의 MW는 얼마인가? 권역이 겹쳐도 합산하지 말고 목록에 표기된 값을 사용하라.

**응답**

> 확인 불가. 제공된 보고서에는 10월 바턴의 RTO 규모 기준 검토에 사용된 최대부하 목록과 보충 목록, 각 권역의 MW가 제시되어 있지 않아 값이 큰 세 권역을 비교하거나 순위를 매길 수 없습니다. 앨라배마·셸비 보고서도 RTO에 대한 셸비의 정책 입장만 다루며, 요청한 부하 수치는 제공하지 않습니다. [Data: Reports (3674)]

**응답이 인용한 보고서**

- 3674 · L2 · Alabama, Gulfstream Pipeline, and Senator Shelby

**정답 (채점 기준)**

> Alliance 81,398 MW → MISO 57,267 MW → PJM 54,000 MW. 24일 목록은 MISO 숫자 뒤에 ‘plus SPP’라고 별도 표기한다. 23일 목록의 SPP 34,000 MW를 더하지 않는다.

원문 근거 번호(연간 CSV): 6731, 6784

## Q09 · 텍사스 전력시장 합병 검토

*상위 몇 개 · 응답 · 62초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 5개*

**질문**

> 11월 ‘Merger Analysis - ERCOT Market Share’ 이메일 대화에서 수치로 명시된 용량이 가장 큰 시설·연계선 두 곳은 어디인가? 각각의 MW를 적고, 그 수치가 계획 규모, 시설 전체 용량, 당시 엔론의 확보·통제 용량 중 무엇을 뜻하는지 설명하라.

**응답**

> **확인 불가.** 제공된 보고서에는 11월 ‘Merger Analysis - ERCOT Market Share’ 이메일 대화의 내용과 발신일이 없어, 그 대화에 용량 수치가 기재된 시설·연계선이 무엇인지, 그중 가장 큰 두 곳이 무엇인지 확인할 수 없습니다. 따라서 아래 수치가 해당 이메일에 등장했거나 그 대화에서 상위 두 값이라고 판단할 근거도 없습니다. [Data: Reports (688, 3920)]
>
> 관련 보고서에서 확인되는 수치를 비교하면 **Comanche Peak 2는 1,150 MW**로, 해당 발전 유닛의 용량입니다. **ERCOT–멕시코 HVDC 연계선은 300 MW**로, 제안된 계획 규모입니다. 이 연계선은 허가 신청이 처리 중이었으며 허가 발급이나 건설·운영은 확인되지 않습니다. 두 수치 모두 당시 Enron이 확보·통제한 용량을 뜻한다고 볼 근거는 없습니다. 다만 이 둘이 지정된 이메일 대화에서 가장 큰 두 수치인지는 확인할 수 없습니다. [Data: Reports (688, 3920, 707)]
>
> 그 밖에 보고서에는 Enron 관련 ERCOT 발전 자산으로 언급된 Ponderosa Pine Energy Partners Ltd의 **263 MW**도 나옵니다. 보고서는 이 수치가 시설 전체 용량인지, 당시 Enron의 확보·통제 용량인지 밝히지 않습니다. 이 수치 역시 지정된 이메일 대화에 포함됐는지는 확인 불가입니다. [Data: Reports (3842)]

**응답이 인용한 보고서**

- 688 · L1 · ERCOT and Texas Electricity Market Transition
- 3920 · L2 · Brownsville Energy Projects: ERCOT–Mexico Tie and Coal Development
- 707 · L1 · Mario Max Yzaguirre, Enron, and Brownsville Energy Projects
- 3842 · L2 · ERCOT, Sam Jones, and Texas Electricity Market Operations

**정답 (채점 기준)**

> ① Brownsville의 ERCOT–멕시코 HVDC 연계선 300 MW. 허가 신청 단계의 계획 규모이며 당시 쓰거나 약정한 용량은 없었다. ② Ponderosa Pine(Cleburne) 263 MW. 발전소 전체 용량이다. 엔론의 지분은 10%였고 이 용량의 통제권은 없었다. 세 번째 후보 Sandhill Austin의 통제 용량은 100 MW다.

원문 근거 번호(연간 CSV): 7610, 7612, 7622, 7624, 7627

## Q10 · 과거 순이익 재작성

*상위 몇 개 · 답 없음(정형 문장) · 41초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 0개*

**질문**

> 11월 엔론이 Form 8-K 제출을 알리며 공유한 순이익 재작성 공지에서, 1997~2000년 연간 순이익의 예상 감소액이 가장 큰 세 회계연도는 언제인가? 감소액을 백만 달러 단위로 적어라.

**응답**

> I am sorry but I am unable to answer this question given the provided data.

**정답 (채점 기준)**

> 1999년 약 250 → 2000년 약 132 → 1998년 약 113(단위 백만 달러). 1997년은 약 96이다. 공지 당시 엔론의 추정치다.

원문 근거 번호(연간 CSV): 7506

## Q11 · 직접구매 중단 기준일

*전부 나열 · 응답 · 58초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 81개*

**질문**

> CPUC의 8월 직접구매 중단 초안과 같은 달 수정 초안이 각각 제시한 기준일을 적어라. 이어 9월 표결이 정한 효력일과 그때도 소급 적용 대상으로 검토 중이던 날짜를 구별해 적어라.

**응답**

> 8월 CPUC 직접구매 중단 초안은 기준일을 **2001년 7월 1일**로 제시했고, 같은 달 수정 초안은 **2001년 9월 20일**을 제시했습니다. [Data: Reports (1488)]
>
> 9월 표결에서 정한 중단 효력일은 **2001년 9월 20일**입니다. 이와 별도로, 중단을 **2001년 7월 1일까지 소급 적용할지는 표결 당시에도 검토 중**이었습니다. 따라서 7월 1일은 확정된 효력일이 아니라 소급 적용 검토 대상 날짜입니다. [Data: Reports (1488, 263, 1655)]

**응답이 인용한 보고서**

- 1488 · L2 · PUC and California Energy Regulation Disputes
- 263 · L1 · CPUC Energy Regulation and Direct Access
- 1655 · L2 · California Power Crisis: Angelides, Procurement and Bond Financing

**정답 (채점 기준)**

> 8월 16일 초안은 9월 1일, 8월 27일 수정 초안은 7월 1일, 9월 20일 표결로 정한 효력일은 9월 20일이다. 7월 1일로 소급할지는 9월 20일 현재 추가 검토 사항이었다.

원문 근거 번호(연간 CSV): 4838, 5030, 5565, 5569

## Q12 · DWR 장기계약 비용

*전부 나열 · 응답 · 61초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 32개*

**질문**

> SP15 피크시간대 선도가격을 기준으로 한 6월 평가와 West Trading 리스크 분석팀의 7월 재평가에서 엔론이 추정한 DWR 계약의 시장가격 초과비용을 모두 적어라. 각 금액의 할인 여부·할인율과 7월 분석의 계약 범위도 밝혀라.

**응답**

> - **6월 평가:** SP15 피크시간대 선도가격을 기준으로 엔론이 추정한 DWR 계약의 시장가격 초과비용은 **확인 불가**입니다. 할인 적용 여부와 할인율도 제공된 보고서에서 확인할 수 없습니다. [Data: Reports (879, 1517, 1884, 3198, 1732, +more)]
>
> - **7월 재평가:** West Trading 리스크 분석팀의 초과비용 추정액, 할인 적용 여부·할인율, 분석 대상 계약의 범위 모두 **확인 불가**입니다. [Data: Reports (879, 1517, 1892, 1732, 80, +more)]
>
> 보고서에 언급된 다른 DWR 계약 가치나 좌초비용 수치는 해당 6월 평가 또는 7월 재평가에서 산출된 초과비용이라고 확인되지 않으므로, 질문의 금액으로 볼 수 없습니다. [Data: Reports (439, 3198, 1892, 1732, 1735, +more)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 879 · L2 · Robert Neustaedter and Enron’s California Energy Analysis
- 1517 · L2 · Sempra and California Gas and Energy Proceedings
- 1884 · L2 · Public Utilities Commissions and California’s Energy Crisis
- 3198 · L2 · El Paso and California Gas Market Proceedings
- 1732 · L2 · DWR and California’s Power Procurement
- 1892 · L2 · Calpine and California Power-Supply Contracts
- 80 · L1 · Enron California Energy Policy Network
- 439 · L1 · Michael Roan, Enron, and Energy-Market Coordination
- 1735 · L2 · DWR Contract Analysis: Coral, Allegheny and Counterparties

**정답 (채점 기준)**

> 6월 분석은 SP15 피크시간대 선도가격 기준 할인 전 210억 달러, 12% 할인 시 130억 달러였다. 7월은 해당 선도곡선과 연 약 4%의 LIBOR를 적용해 약 100억 달러로 추산했다. 체결 계약만 포함하고 원칙적 합의 단계 계약은 제외했다. 가스가격 연동 계약에서는 가스비 전가분을 제외한 비용만 평가했다.

원문 근거 번호(연간 CSV): 3394, 4021

## Q13 · PG&E 채권 신고와 재편안

*전부 나열 · 응답 · 66초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 57개*

**질문**

> 5월 PG&E의 Schedule F에서 분쟁 중이라고 기재된 PX 크레딧 가운데 개별 엔론 법인의 금액이 명시된 항목을 모두 적어라. 금액은 가장 가까운 백만 달러로 반올림하라. 이어 9월 법원에 제출된 재편안에서 변제 방식이 명시된 채권자 범주와 범주별 현금·장기어음 비율을 모두 적어라.

**응답**

> ### 5월 PG&E Schedule F의 분쟁 중 PX 크레딧
>
> 개별 Enron 법인의 금액이 명시된 항목은 다음과 같습니다.
>
> - **Enron Energy Marketing:** $201,964,905.64, 가장 가까운 백만 달러로 반올림하면 **약 2억 2백만 달러**입니다. [Data: Reports (1439)]
> - **Enron Energy Services:** $19,737,979.97, 반올림하면 **약 2천만 달러**입니다. [Data: Reports (1260, 209)]
>
> ### 9월 법원 제출 재편안의 변제 방식
>
> 보고서에 변제 방식이 명시된 채권자 범주는 다음과 같습니다.
>
> - **채권액이 10만 달러를 초과하는 채권자:** 현금 **60%**, 채권(bonds) **40%**로 기재되어 있습니다. [Data: Reports (1434)]
> - **대부분의 담보채권자:** 허용된 채권액의 현금 **100%**, 장기어음 **0%**로 기재되어 있습니다. [Data: Reports (1797)]
>
> 다른 채권자 범주의 변제 방식이나 비율은 제공된 보고서에서 확인할 수 없습니다.

**응답이 인용한 보고서**

- 1439 · L2 · PG&E Bankruptcy, Creditors, and California Restructuring
- 1260 · L2 · Enron Energy Services: Energy Markets, Customers, and Oversight
- 209 · L1 · Enron Environmental Strategies and Energy Services Network
- 1434 · L2 · PG&E Bankruptcy and Reorganization
- 1797 · L2 · California Energy Disputes and Bankruptcy Proceedings

**정답 (채점 기준)**

> 5월에 금액이 적힌 두 분쟁 중 PX 크레딧은 Enron Energy Marketing 약 202백만 달러(원문 $201,964,905.64)와 Enron Energy Services 약 20백만 달러(원문 $19,737,979.97)다. 9월 제출안에서 10만 달러 이하 인정 채권은 현금 100%, 대부분의 담보부 채권자도 현금 100%, 10만 달러 초과 무담보 인정 채권은 현금 60%·장기어음 40%다.

원문 근거 번호(연간 CSV): 2919, 5558

## Q14 · 미 동남부 송전기구 조정

*전부 나열 · 응답 · 73초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 66개*

**질문**

> 3월 말 FERC가 조건부 승인하거나 거절한 동남부 지역 송전기구(RTO)의 전체 구성안을 나열하고 각각 어떤 결정을 내렸는지 적어라. 7월의 동남부 단일 RTO 조정에서는 이름이 명시된 RTO들을 참여 의무와 권고로 구분하라.

**응답**

> ### 3월 말 FERC 결정
>
> 제공된 보고서로는 3월 말 FERC가 검토한 동남부 RTO **전체 구성안 목록과 각 안건의 처분을 빠짐없이 확인할 수 없습니다.** 확인되는 3월 28일 결정은 SPP와 Entergy가 제안한 공동 RTO를 거절한 것입니다. FERC는 제안의 범위와 구성이 Order No. 2000의 요건을 충족하지 못한다고 판단했고, 보고된 제안의 전체 참여자 구성은 자료에 제시되어 있지 않습니다. [Data: Reports (381, 2352, 2555, 2383, 399)]
>
> GridSouth 안은 FERC가 조건부 승인한 것으로 기록되어 있습니다. 보고서에 기재된 조건에는 조직 규모 확대, 독립 이사회 구성, 회원 및 이사회 선정 절차 관련 조정, 준수 자료 제출 등이 포함됩니다. 다만 이 결정이 3월 말에 내려졌다는 날짜는 보고서에서 확인되지 않으므로, 3월 말 결정으로 단정할 수 없습니다. [Data: Reports (2557, 399, 2558, 2428)]
>
> Southern Company의 RTO 제안도 보고서에 언급되지만, FERC가 그 범위를 불충분하다고 판단해 조정 절차로 보냈다는 기록과 제안을 거절했다는 기록이 함께 있습니다. 해당 처분이 질문에서 지정한 3월 말 결정에 해당하는지, 그리고 전체 구성안이 무엇이었는지는 확인 불가입니다. 따라서 이 자료만으로 3월 말에 조건부 승인·거절된 모든 구성안을 완전하게 나열할 수는 없습니다. [Data: Reports (2383, 2413, 410)]
>
> ### 7월 동남부 단일 RTO 조정
>
> 한 보고서는 참여 의무 대상 RTO를 **Grid South, SE Trans, SETrans**, 참여 권고 대상 RTO를 **Grid Florida**로 구분합니다. 해당 보고서가 SE Trans와 SETrans를 서로 다른 표기로 적고 있으므로 그대로 구분해 기재합니다. [Data: Reports (2557)]
>
> 다만 다른 관련 보고서들은 7월 조정의 RTO별 참여 의무·권고 명단을 제시하지 않습니다. 따라서 위 구분은 해당 명단을 직접 밝힌 보고서에 근거하며, 제공된 자료만으로 그 목록이 더 있는지 또는 표기 차이가 별도 RTO를 뜻하는지 확인할 수는 없습니다. [Data: Reports (2520, 2521, 2352, 2363, 2522)]

**응답이 인용한 보고서**

- 381 · L1 · FERC, Enron, and Energy-Market Regulation
- 2352 · L2 · FERC, Enron, and U.S. Energy Regulation
- 2555 · L2 · Entergy, SPP, and Regional Transmission Organization Proceedings
- 2383 · L2 · FERC Review of SPP, Entergy, and Southern Company RTO Proposals
- 399 · L1 · SPP, Enron, and Southeast RTO Regulatory Community
- 2557 · L2 · Southeast RTO Mediation: Bobbie McCartney and Grid South
- 2558 · L2 · GridSouth and Southeast RTO Proposals
- 2428 · L2 · FERC Market, RTO, and Pipeline Regulation
- 2413 · L2 · Southeast RTO Orders and Southern Company
- 410 · L1 · Southern Company Services, FERC, and Gulf Power Interconnection
- 2520 · L2 · Southeast RTO and FERC Grid Reorganization
- 2521 · L2 · Southeast RTO Proceeding and Mediation
- 2363 · L2 · FERC, Commissioner Brownell, and the SE RTO
- 2522 · L2 · Southeast RTO Mediation and Enron

**정답 (채점 기준)**

> 3월에는 GridFlorida 제안을 조건부 승인하고 SPP·Entergy 공동 제안을 거절했다. 7월 조정에 의무적으로 참여하도록 한 곳은 GridSouth, SETrans, SPP다. GridFlorida에는 참여를 권고했다.

원문 근거 번호(연간 CSV): 1485, 1487, 4019

## Q15 · 9월 출장 직원 귀가 지원

*전부 나열 · 응답 · 49초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 4개*

**질문**

> 9·11 이후 귀가가 어려워진 출장 직원에게 엔론은 어디에서 정보를 구하라고 했고, 이동 비용과 체류 연장에 관해 어떤 지원을 안내했나? 후속 여행 지원 현황에서 보고한 예약과 주말 운영 조치도 모두 적어라.

**응답**

> 9·11 이후 귀가에 어려움을 겪는 출장 직원은 **Travel Agency in the Park**에서 여행 정보를 얻고 도움을 받을 수 있다고 안내받았다. 여행사는 전화 지원을 제공하고 항공편과 숙박을 마련했으며, 트레이시 램지와 직원들도 출장 직원들이 안전하게 귀가하도록 여행사와 협력하겠다고 했다. [Data: Reports (1144)]
>
> 후속 지원 현황에는 항공편과 숙박을 마련했다는 내용이 있지만, 실제 예약 건수나 예약별 세부 사항은 **확인 불가**다. 주말에도 여행사는 24시간 운영을 유지하고 전담 비상 인력을 두겠다고 보고했다. [Data: Reports (1144)]
>
> 이동 비용을 누가 부담하는지, 비용 지원이 제공되는지, 직원이 체류를 연장할 때 어떤 지원을 받을 수 있는지는 **확인 불가**다. [Data: Reports (1144)]

**응답이 인용한 보고서**

- 1144 · L2 · Amy Kim, Tracy Ramsey, and Enron Coordination

**정답 (채점 기준)**

> 12일에는 사내 웹사이트와 24시간 운영하는 Travel Agency in the Park에서 정보를 확인하라고 했다. 안전하고 합리적인 귀가 교통편의 비용을 상환하고 필요하면 체류를 연장할 수 있다고 안내했다. 14일에는 협력 여행사들이 24시간 요청에 응답하고 항공편과 숙소를 예약했으며, 사내 담당팀과 여행사가 주말에도 지원을 계속할 계획이라고 보고했다.

원문 근거 번호(연간 CSV): 5335, 5402

## Q16 · 미국 발전소 다중오염물질 규제안

*전부 나열 · 응답 · 48초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 18개*

**질문**

> 8월에 공유된 Clean Power Group의 발전소 규제안에서 의무 배출 상한과 전국 배출권거래를 적용하자고 제안한 오염물질을 모두 나열하라. CO₂ 감축의 성격과 배출권 가격이 기준을 넘을 때 적용하는 조치도 밝혀라.

**응답**

> 8월에 공유된 Clean Power Group 발전소 규제안은 **질소산화물(NOx), 이산화황(SO₂), 수은**에 전국적인 의무 배출 상한과 배출권거래를 적용하는 방안을 제안했습니다. [Data: Reports (3033)]
>
> **CO₂ 감축은 의무가 아니라 선택 사항**으로 제시됐습니다. [Data: Reports (3032, 485)] 배출권 가격이 정해진 기준(‘circuit-breaker’ 수준)을 넘으면 **감축을 일시 중단**하는 조치가 포함됐습니다. 다만 그 가격 기준이 얼마인지는 확인할 수 없습니다. [Data: Reports (3032, 3033)]

**응답이 인용한 보고서**

- 3033 · L2 · Enron and the Clean Power Group Multipollutant Initiative
- 3032 · L2 · Clean Energy Group and Power-Plant Emissions Proposals
- 485 · L1 · Enron, Jeff Keeler, and Multipollutant Policy

**정답 (채점 기준)**

> 질소산화물(NOx)·이산화황(SO₂)·수은(Hg)이 의무 배출 상한 및 배출권거래 대상에 포함하는 안이었다. CO₂ 감축은 선택적으로 도입할 수 있는 방안으로 제안됐다. 특정 오염물질의 배출권 가격이 기준을 넘으면 해당 물질의 감축을 일시 동결하고, 가격이 기준 밑으로 내려가면 감축을 재개하는 구상이었다.

원문 근거 번호(연간 CSV): 4691, 4718

## Q17 · 다이너지 합병 발표의 투자 계획

*전부 나열 · 응답 · 57초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 15개*

**질문**

> 11월 엔론과 다이너지의 합병 발표에 명시된 신규 투자 약정을 모두 적어라. 각 투자 약정의 투자자·대상·금액·시점과 우선주 조건을 구별하라.

**응답**

> ### 확인되는 신규 투자 약정
>
> 11월 9일 합병 제안 발표에 명시된 것으로 확인되는 신규 투자 약정은 한 건입니다. 투자자는 다이너지, 투자 대상은 엔론 자회사인 Northern Natural Gas이며, 금액은 15억 달러입니다. 대가는 우선주로 명시되어 있습니다. 투자 집행 시점이나 일정은 확인 불가하며, 실제 투자가 완료됐는지도 확인되지 않습니다. [Data: Reports (176, 1186)]
>
> 우선주의 종류·배당 등 구체 조건은 확인 불가입니다. 별도 기록에는 다이너지가 우선주와 추가 권리를 받았다고 되어 있으며, 합병이 무산될 경우 해당 계열사를 인수할 수 있는 옵션과 우선주를 파이프라인 계열사 주식 또는 엔론 주식으로 추가 대가 없이 전환할 권리가 언급됩니다. 다만 이 권리의 실제 행사 여부는 확인되지 않습니다. [Data: Reports (2217)]
>
> 다이너지의 엔론 대상 15억 달러 현금 지원이나 ChevronTexaco의 다이너지 자금 조달 지원·추가 투자 계획도 별도 기록에 나오지만, 이들이 11월 합병 발표에 명시된 신규 약정이라는 점은 확인되지 않으므로 위 약정에 추가하지 않습니다. [Data: Reports (2206, 2217, 348, 1180)]

**응답이 인용한 보고서**

- 176 · L1 · Enron–Dynegy Merger and Energy Trading Community
- 1186 · L2 · Northern Natural Gas, Dynegy Investment, and OFO
- 2217 · L2 · Dynegy, Enron, and California Power-Market Controversies
- 2206 · L2 · Enron's Conference Calls and Dynegy Cash Infusion
- 348 · L1 · Enron Corp. and Its Energy-Market Network
- 1180 · L2 · Dynegy–Enron Merger and Energy-Regulatory Community

**정답 (채점 기준)**

> ① ChevronTexaco → Dynegy에 즉시 15억 달러 ② ChevronTexaco → Dynegy에 합병 종결 시 추가 10억 달러 ③ Dynegy → 엔론 자회사 Northern Natural Gas에 즉시 현금 15억 달러, 그 대가로 해당 자회사 우선주 취득. 발표문에 적힌 계획과 종결 조건을 기준으로 한다.

원문 근거 번호(연간 CSV): 7546

## Q18 · 거래상대방 담보

*전부 나열 · 응답 · 53초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 37개*

**질문**

> 11월 말 EES의 담보 요구 현황에서 신용관리팀(Credit)에 최근 2주간 증거금 문제로 연락한 사업자와, Risk Desk의 ISO 담보 지원 안내에서 담당자를 지정한 시장을 각각 모두 나열하라.

**응답**

> - **최근 2주간 증거금 문제로 Credit에 연락한 사업자:** 확인 불가. 보고서에는 11월 19일 Niagara Mohawk가 EES에 430만 달러의 증거금을 요구했다는 내용이 있지만, Niagara Mohawk가 해당 기간에 Credit에 연락했는지는 확인되지 않습니다. [Data: Reports (874, 1203, 203, 1366, 226, +more)]
>
> - **Risk Desk의 ISO 담보 지원 안내에서 담당자를 지정한 시장:** ERCOT—Sanjay Hemani, PJM—Michelle Raque, NYISO—Juan Padron. [Data: Reports (1079)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 874 · L2 · Enron California Energy Affairs: Harry Kingerski and Marty Sunde
- 1203 · L2 · Enron Energy Services (EES) and Its Energy Markets
- 203 · L1 · Enron Energy Services and Stacey Bolton
- 1366 · L2 · Niagara Mohawk, EES Margin Call, and Tractabel Power-Supply Deal
- 226 · L1 · Niagara Mohawk, Andersen, and Energy-Industry Policy
- 1079 · L2 · Enron Risk Group, Juan Padron, and NYISO Credit

**정답 (채점 기준)**

> 신용관리팀에 연락한 곳은 SoCal, NIMO, BGE다. Risk Desk가 담당자를 지정한 시장은 NEPOOL, ERCOT, PJM, NYISO다.

원문 근거 번호(연간 CSV): 8050, 8141

## Q19 · 12월 추가 파산 신청 법인

*전부 나열 · 응답 · 38초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 2개*

**질문**

> 12월 엔론의 추가 파산 신청 안내와 같은 날 보낸 법인명 정정 메일을 종합하면, 안내에 적힌 신청 법인들의 최종 명칭은 무엇인가? 모두 적어라.

**응답**

> 최종 명칭은 **Enron Energy Information Solutions, Inc., Enron Merchant Investments, Inc., Tenant Services, Inc., Enron Federal Solutions, Inc.**입니다. 같은 날 발송된 정정 메일은 안내문에 적힌 “Enron Energy Solutions, Inc.”를 “Enron Energy Information Solutions, Inc.”로 수정했으며, 나머지 세 법인명은 바뀌지 않았습니다. [Data: Reports (36)]

**응답이 인용한 보고서**

- 36 · L0 · Enron-Affiliated Bankruptcy Filings and Name Correction

**정답 (채점 기준)**

> Tenant Services, Inc. / Enron Federal Solutions, Inc. / Enron Energy Information Solutions, Inc. / Enron Merchant Investments, Inc. 첫 안내의 ‘Enron Energy Solutions, Inc.’는 세 번째 법인명의 오기이므로 별도 항목으로 세지 않는다.

원문 근거 번호(연간 CSV): 8387, 8388

## Q20 · 다볼 미지급금과 지급보증

*전부 나열 · 응답 · 61초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 51개*

**질문**

> 1~2월 다볼 발전사업 메일에서 미지급 전력 대금의 보증 청구 대상으로 등장한 정부를 모두 적어라. 각 상대에게 취한 조치와 원문에서 확인할 수 있는 날짜를 밝히고, 실제 청구일과 이메일 보고일이 다르면 구별하라.

**응답**

> ### 확인 가능한 정부와 조치
>
> **인도 중앙정부(연방정부)**는 확인 가능한 보증 상대입니다. 보고서에는 MSEB가 지급을 불이행하면 1996년 반대보증(counter-guarantee)에 따라 중앙정부가 Enron에 지급해야 한다는 내용이 있습니다. 별도 기록은 Enron India가 미지급 전력 대금을 회수하기 위해 중앙정부 보증을 청구하거나 발동하려 했다고 설명합니다. 한 기록은 이메일에 보증이 “전날 청구됐다”고 적혀 있다고 하지만, 청구일과 이메일 발신일의 구체적인 날짜는 확인되지 않습니다. 따라서 이 조치가 질문의 2001년 1~2월 메일에 해당하는지는 확인 불가입니다. [Data: Reports (423, 2736, 2696, 2677, 433, +more)]
>
> **마하라슈트라주 정부**도 별도 보고서에서 보증 청구 대상으로 언급됩니다. DPC가 11월분 미지급 전력 대금과 관련해 주정부 보증을 청구하겠다고 통지했다는 기록이 있으나, 통지 날짜와 실제 청구 여부는 확인되지 않습니다. 다른 기록은 주정부 보증을 실제로 사용한 날짜를 2001년 8월 29일로, 중앙정부 보증을 사용한 날짜를 2001년 9월 7일로 제시합니다. 이 두 날짜는 1~2월보다 뒤이므로, 해당 조치가 질문에서 지정한 1~2월 메일에 담겼다고 볼 수는 없습니다. [Data: Reports (2672, 2683, 2737)]
>
> ### 날짜와 범위의 한계
>
> 제공된 보고서에는 질문의 1~2월 메일 발신일이 제시되어 있지 않고, 실제 보증 청구일과 이메일 보고일을 서로 대조할 날짜도 없습니다. 따라서 **해당 메일에 보증 청구 대상으로 등장한 정부의 전체 목록과 각 정부에 취한 조치를 확정할 수 없습니다.** 중앙정부는 보증 청구·발동 관련 기록에서 확인되며, 마하라슈트라주 정부도 별도 보증 통지 기록에 등장하지만, 두 정부 모두를 질문의 메일 범위에 속한다고 단정할 근거는 없습니다. [Data: Reports (2696, 2736, 2672, 2683, 2740, +more)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 423 · L1 · Enron, Dabhol, and India’s Power-Sector Dispute
- 2736 · L2 · Enron India, MSEB, and the Dabhol Dispute
- 2696 · L2 · Enron, Dabhol, and India’s Power-Sector Dispute
- 2677 · L2 · Dabhol Power Company, Enron, and the MSEB Dispute
- 433 · L1 · Enron–Dabhol Dispute: Maharashtra and IDBI
- 2672 · L2 · Government of Maharashtra–Dabhol Dispute and Enron Probe
- 2683 · L2 · Enron, Dabhol Power Co. and the MSEB Dispute
- 2737 · L2 · Maharashtra–Enron Dabhol Power-Payment Dispute
- 2740 · L2 · India's Federal and State Electricity Finance

**정답 (채점 기준)**

> 1월 25일 메일은 마하라슈트라 주정부에 보증 청구 통지를 보냈다고 보고했다. 인도 중앙정부 보증 청구는 2월 5일에는 다음 날의 계획으로 언급됐으며, 2월 7일 메일이 실제 청구일을 전날인 2월 6일로 확인했다.

원문 근거 번호(연간 CSV): 332, 473, 525

## Q21 · 직접구매 중단과 기존 계약 검증

*추세 · 응답 · 77초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 203개*

**질문**

> 6월 엔론 법무·규제팀은 직접구매 중단을 앞두고 기존 계약의 서비스 신청(DASR), 신규 계약의 서명과 서비스 신청에 대해 각각 무엇을 권고했나? 9월 중단 결정 뒤인 10월 초에는 기존 계약의 서비스 신청이 유효한지 어떤 방식으로 확인하려 했나?

**응답**

> ### 6월 권고
>
> 확인 불가. 제공된 보고서에는 엔론 법무·규제팀이 **기존 계약의 DASR**, **신규 계약의 서명**, **신규 계약의 서비스 신청(DASR)**을 각각 어떻게 처리하라고 권고했는지가 기록되어 있지 않습니다. 직접구매 중단을 둘러싼 정책·규제 논의가 언급되더라도, 계약 유형별 권고를 확인할 근거는 없습니다. [Data: Reports (1595, 252, 1684, 2195, 2596, +more)]
>
> ### 9월 결정 이후, 10월 초 확인 방식
>
> 기존 계약의 DASR이 유효한지 확인하려 한 구체적인 절차·자료·담당 주체는 확인 불가입니다. 다만 10월 2일에는 에너지 서비스 제공업체, 유틸리티, CPUC 에너지부서 직원들이 중단 명령의 이행을 논의했고, DASR을 계속 제출할지, 고객 명단 및 가능한 cutoff date를 어떻게 다룰지가 논의 주제에 포함됐습니다. 이 기록은 회의에서 다룬 사안을 보여줄 뿐, 기존 DASR의 유효성을 실제로 검사하거나 판단한 방법을 밝히지는 않습니다. [Data: Reports (1543)]
>
> 또한 자료만으로는 질문에 전제된 9월 중단 결정의 정확한 시점과 구체적 내용을 일관되게 확인할 수 없습니다. 일부 보고서는 중단 명령을 언급하지만, 다른 보고서는 표결이 예정되거나 연기될 것으로 예상됐다고 하며 최종 결정 여부를 확인해 주지 않습니다. [Data: Reports (1654, 1683, 1703, 1666, 2625)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 1595 · L2 · DA Suspension, California PUC, and Angelides Investor Memo
- 252 · L1 · California Direct-Access Policy Dispute: CPUC, ESPs, and Business Customers
- 1684 · L2 · California Power Purchasing, DWR, and AB 1X
- 2195 · L2 · Enron Corp.: Energy Markets, Oversight, and Financial Crisis
- 2596 · L2 · Utility Regulation: New York Unbundling and Rehearing Proceedings
- 1543 · L2 · CPUC Direct-Access Suspension Meeting
- 1654 · L2 · California Public Utilities Commission and the Energy Crisis
- 1683 · L2 · California AB1X, DWR Power Purchases, and Direct Access
- 1703 · L2 · California Legislature and Energy Policy
- 1666 · L2 · California Direct-Access Contracts and PUC Suspension Debate
- 2625 · L2 · California CPUC Direct Access Proposal and Duque–Bilas Dissent

**정답 (채점 기준)**

> 6월 법무·규제팀은 기존 계약의 서비스 신청(DASR)을 중단 전에 제출하고, 신규 계약은 양측 서명을 마친 뒤 DASR을 신속히 내라고 권고했다. 당시 권고는 기존 계약 신청 6월 29일, 신규 계약 서명 6월 30일, 신규 계약 신청 7월 6일까지였다. 10월에는 기존 계약에 시설을 추가·삭제할 수 있다는 점을 고려해 고객 명단과 계정 정보를 받아 신청을 대조하는 방안을 논의했다. 목록 밖 계정에는 진술서 등 별도 검증을 적용하는 방안도 나왔으며, 처리 규칙을 위해 CPUC에 공동 신청을 추진하기로 했다.

원문 근거 번호(연간 CSV): 3450, 5565, 5928

## Q22 · DWR 계약 비용과 소비자 요금

*추세 · 응답 · 105초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 510개*

**질문**

> 6~7월 엔론은 DWR 장기계약의 비용을 어떤 가격과 비교해 평가했나? 8~10월에는 그 비용을 소비자 요금에 반영하는 절차가 어떻게 쟁점이 됐나? PG&E의 법원 요청과 CPUC의 표결을 구별하라.

**응답**

> ### 6~7월: 엔론의 비용 비교
>
> 확인 불가. 제공된 보고서에는 엔론이 DWR 장기계약 비용을 어떤 가격과 비교했는지, 또는 평가한 시점과 방식을 특정할 정보가 없다. 따라서 현물가격·선도가격 등 어떤 기준을 사용했는지도 확인할 수 없다. ENA와 DWR의 5주 단기계약 및 검토 중이었으나 서명되지 않은 5년 연장 가능성이 언급되지만, 비용 비교 기준은 제시되지 않는다. [Data: Reports (1684, 938, 2206, 743, 1892, +more)]
>
> ### 8~10월: 소비자 요금 반영
>
> 확인 불가. 이 기간에 DWR 장기계약 비용을 소비자 요금에 반영하는 절차가 어떻게 쟁점이 됐는지, 누가 어떤 조치를 했는지, 시기별로 무엇이 달라졌는지 설명하는 자료가 없다. 일반적인 요금 동결·할증료 또는 요금 구조 논의는 언급되지만, 이를 DWR 계약 비용의 요금 반영 절차로 연결할 근거는 없다. [Data: Reports (1203, 2284, 1465, 1533, 255, +more)]
>
> ### PG&E의 법원 요청과 CPUC 표결
>
> 두 조치는 구별해야 하지만, 질문에서 가리키는 PG&E의 법원 요청과 CPUC 표결은 각각 내용·날짜·결과를 확인할 수 없다. 한 보고서는 SCE의 PX 크레딧 처리와 PG&E의 유사한 조치가 예상된다는 맥락에서 Charley Ferguson이 법원 또는 CPUC에 이의를 제기할지 검토하고 대안 소장을 준비하려 했다고 기록한다. 이는 PG&E가 법원에 요청했다는 기록이 아니다. 별도로, 직접접속 중단 사안에 관한 CPUC 표결이 예정됐다는 기록은 있으나 날짜와 결과는 확인되지 않으며, PX 크레딧 문제와도 구분된다. [Data: Reports (252, 1674, 919)]
>
> 또한 보고서에 나오는 CPUC의 5대 0 표결은 SoCal이 적격시설(QF)에 미지급액의 15%를 지급하도록 한 별도 사안으로, 질문의 PG&E 법원 요청이나 DWR 비용 관련 표결로 볼 수 없다. [Data: Reports (1720)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 1684 · L2 · California Power Purchasing, DWR, and AB 1X
- 938 · L2 · Enron’s California Energy and Regulatory Network
- 2206 · L2 · Enron's Conference Calls and Dynegy Cash Infusion
- 743 · L2 · Enron’s California Policy Network: Jeff Dasovich and Colleagues
- 1892 · L2 · Calpine and California Power-Supply Contracts
- 1203 · L2 · Enron Energy Services (EES) and Its Energy Markets
- 2284 · L2 · The Wall Street Journal and Its Energy Reporting Network
- 1465 · L2 · AB1890 Rate Freeze and 3¢/kWh Surcharge
- 1533 · L2 · Southern California Edison and CPUC Rate Proceedings
- 255 · L1 · CPUC Rate Design Hearing and Stakeholders
- 252 · L1 · California Direct-Access Policy Dispute: CPUC, ESPs, and Business Customers
- 1674 · L2 · CPUC DA Suspension Issue and Anticipated Vote
- 919 · L2 · Mike Day and California Energy Regulation
- 1720 · L2 · California Qualifying Facilities and Utility Payment Crisis

**정답 (채점 기준)**

> 엔론은 장기계약 비용을 시장 선도가격과 비교해 초과비용을 추정했다. 8월 21일 PG&E는 130억 달러 규모의 계약비용을 소비자에게 부과하기 전에 DWR가 공개 심리를 열도록 법원에 요청했다. 10월 2일 CPUC는 계약비용을 요금에 전가하는 DWR와의 요금 협약안을 4 대 1로 부결했다.

원문 근거 번호(연간 CSV): 3394, 4021, 4910, 5883

## Q23 · PG&E 파산 절차와 사업 분리

*추세 · 응답 · 74초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 91개*

**질문**

> 4월 PG&E의 Chapter 11 신청 직후 법원이 영업 지속을 위해 허용한 조치는 무엇이었나? 9월 제출된 재편안에서는 배전·가스 배급과 발전·전력 송전·가스 수송을 어떻게 배분했고, 캘리포니아 당국은 왜 반대했나?

**응답**

> ### 4월 Chapter 11 신청 직후
>
> PG&E는 2001년 4월 6일 Chapter 11 재편을 신청한 것으로 보고되어 있다. 그러나 신청 직후 법원이 영업을 계속하도록 허용한 구체적 조치나 명령은 제공된 보고서에서 **확인 불가**다. 법원이 임시 현금담보 사용이나 천연가스 관련 수입을 다루는 절차를 진행했다는 언급은 있으나, 실제로 어떤 조치를 허용했는지는 명시되어 있지 않다. [Data: Reports (1777, 93)]
>
> ### 9월 재편안과 당국의 반대
>
> 9월 20일 PG&E와 PG&E Corporation이 파산법원에 재편안을 공동 제출했다는 보고가 있다. 다만 보고서는 그 제출 사실과 채권자 청구 처리를 다룰 뿐, 질문에 든 사업 부문을 모두 어떻게 나눴는지는 완전히 밝히지 않는다. [Data: Reports (1797)]
>
> 재편 구상에서는 발전 및 전력 송전 자산을 비규제 모회사 또는 계열사로 옮기고, 별도의 재편 유틸리티를 두는 내용이 보고되어 있다. 별도 모회사가 발전·전력 송전·가스 송전 사업을 보유할 구상도 언급된다. 그러나 배전과 가스 배급을 어느 법인에 배정했는지, 또는 가스 수송의 구체적 귀속이 무엇이었는지는 자료만으로 확정할 수 없다. 따라서 각 부문의 완전한 배분은 **확인 불가**다. 이 계획은 법원 승인 등 조건에 따른 제안이었으며 실제 시행이 확정된 것은 아니다. [Data: Reports (1434, 1777, 99)]
>
> 캘리포니아 공공사업위원회(PUC/CPUC) 등 당국의 반대와 관련해 보고된 핵심 우려는 자산을 비규제 계열사로 이전하면 주 정부의 감독 권한이 약해질 수 있다는 점이다. PUC 법률고문은 제안된 자산 이전에 PUC 승인이 필요하다고 밝혔고, 자산 가치 평가도 비판했다. 이는 규제 권한과 평가에 대한 우려이지, 법원이 위법을 확정했다는 뜻은 아니다. [Data: Reports (1434, 1417)]

**응답이 인용한 보고서**

- 1777 · L2 · PG&E, California’s Energy Crisis, and Chapter 11 Reorganization
- 93 · L1 · Enron Regulatory Strategy, California Energy Markets, and GMSSR Contacts
- 1797 · L2 · California Energy Disputes and Bankruptcy Proceedings
- 1434 · L2 · PG&E Bankruptcy and Reorganization
- 99 · L1 · Barry Bonds and the San Francisco Giants
- 1417 · L2 · PG&E Bankruptcy, PUC, and Edison Settlement

**정답 (채점 기준)**

> 4월에는 가스 판매수입을 향후 가스 공급 확보에 사용하고 현금 담보를 정상 영업에 잠정 사용할 수 있도록 법원이 허용했다. 9월안은 Pacific Gas and Electric Company에 배전·가스 배급을 남기고, 별도 회사인 PG&E Corporation 산하로 발전·전력 송전·가스 수송을 옮기겠다는 내용이었다. 전달 기사에 따르면 데이비스 주지사와 CPUC 측은 발전자산 등에 대한 주 규제 권한이 줄어드는 데 반대했다.

원문 근거 번호(연간 CSV): 1636, 1734, 5558, 5579

## Q24 · 캘리포니아 도매전력 환급 절차

*추세 · 응답 · 97초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 495개*

**질문**

> 캘리포니아 도매전력 환급 절차는 6월 말 합의 협상 개시 이후 7월 행정판사의 권고와 FERC의 조치를 거쳐 어떻게 바뀌었나? 10월 진행 상황 보고에 남아 있던 산정 쟁점과 자료 문제, 12월 FERC가 심리를 정지한 이유를 설명하라.

**응답**

> 확인되는 경과는 다음과 같습니다. 6월 말 협상 개시일은 자료에서 확인되지 않지만, FERC가 중재한 환급 합의 협상은 15일간 진행된 뒤 2001년 7월 9일 합의 없이 끝났다. 캘리포니아는 89억 달러를 요구했고, 전력 공급자들의 제안액은 합계 7억 1,610만 달러여서 큰 격차가 남았다. [Data: Reports (382)]
>
> 2001년 7월 12일 수석 행정판사는 환급 산정 및 증거 제출 절차를 권고했다. 권고안은 2000년 10월 2일부터 2001년 5월 28일까지의 캘리포니아 현물시장 판매를 대상으로 시간별 경쟁가격을 다시 계산하고, 해당 기간의 구매자·판매자 정산액을 재산정·재정산하는 방안을 담았다. 이는 권고였으며, 이 자료만으로는 최종 환급 결정이나 금액이 확정됐다고 볼 수 없다. [Data: Reports (2461)]
>
> 그 뒤 FERC는 환급액 산정 심리를 추가 명령이 있을 때까지 정지했고, 재심 요청이 계류 중인 동안 심리는 무기한 멈춘 것으로 보고되어 있다. 따라서 절차는 산정 심리를 진행하는 상태에서 정지 상태로 바뀌었다. 다만 이 보고서는 정지 명령의 날짜를 특정하지 않으므로, 이를 12월 조치로 확정할 수는 없다. 재심 요청이 계류 중이었다는 점은 확인되지만, 그 외의 구체적인 정지 사유는 확인 불가다. [Data: Reports (2378)]
>
> 10월 진행 상황 보고에 남아 있던 환급액 산정 쟁점이나 자료 문제는 제공된 보고서에서 확인할 수 없다. 따라서 당시 어떤 산정 방식에 이견이 있었는지, 어떤 자료가 누락·부족했는지 설명할 근거가 없다. [Data: Reports (428, 677, 2119, 3197, +more)]
>
> 또한 제공된 자료 중 환급 관련 일부 내용은 태평양 북서부 사건을 다루므로, 이를 캘리포니아 절차의 경과로 간주할 수 없다. [Data: Reports (2564, 2565)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 382 · L1 · California Power Refunds and FERC Market Proceedings
- 2461 · L2 · Cal PX, FERC Proceedings, and California Electricity Refunds
- 2378 · L2 · FERC Stay of the California Refund Hearing
- 428 · L1 · FERC Refund Appeals: Alliant Energy and Nebraska Public Power District
- 677 · L1 · Seattle Energy Infrastructure and Regulatory Meetings
- 2119 · L2 · Washington, D.C., Enron Offices, and Energy Policy
- 3197 · L2 · State Utilities Commission Investigation and California Case
- 2564 · L2 · Pacific Northwest Refund Cases and FERC ALJ Proceedings
- 2565 · L2 · FERC Pacific Northwest Spot Power Sales Refund Investigation

**정답 (채점 기준)**

> 6월 25일 주 당국과 전력공급자 간 합의 협상이 시작됐다. 7월 합의가 이뤄지지 않자 행정판사는 환급 대상과 기간, 상계 등을 권고했다. FERC는 증거심리에서 산정에 필요한 자료를 수집하도록 했다. 10월에는 적용할 시장가격, 판매자별 금액과 상계액이 쟁점이었고 CAISO 자료의 오류·누락으로 심리가 지연됐다. 12월 6일 FERC는 계류 중인 재심 요청을 받아들이면 환급액 계산이 달라질 수 있어 추가 명령 때까지 심리를 정지했다.

원문 근거 번호(연간 CSV): 3547, 4065, 4421, 6907, 8232

## Q25 · 미 동북부 지역 송전기구 통합

*추세 · 응답 · 84초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 339개*

**질문**

> 미 동북부 지역 송전기구(RTO)를 단일화하는 과정에서 5월 엔론의 제안, 7월 FERC의 판단과 조정 지시, 9월 조정 판사의 권고는 어떻게 달랐나? 각 단계가 다룬 통합 기반이나 시장 설계의 주체를 밝혀라.

**응답**

> 제공된 보고서만으로는 **5월 엔론의 제안, 7월 FERC의 판단·조정 지시, 9월 조정 판사의 권고를 완전하게 비교할 수 없습니다.** 특히 5월 제안의 구체적 내용과 통합 기반·시장 설계의 주체, 7월 FERC 조치의 내용과 대상은 확인되지 않습니다. [Data: Reports (2520, 2437, 2778, 2026, 2833, +more)]
>
> **5월 — 엔론의 제안:** 제안의 구체적 내용이나 어떤 통합 기반 또는 시장 설계를 제시했는지는 확인 불가입니다. 별도 보고서에는 NYISO, PJM, NEPOOL을 하나의 Northeast ISO로 통합하자는 제안과 그에 대한 FERC 계류 중 항의가 언급되지만, 제안자와 날짜가 밝혀져 있지 않아 이를 엔론의 5월 제안으로 연결할 수 없습니다. [Data: Reports (2542, 2520)]
>
> **7월 — FERC의 판단·조정 지시:** 해당 동북부 RTO 사안에 대한 7월 판단이나 지시의 내용, 그리고 조정 대상이 된 통합 기반 또는 시장 설계 주체는 확인 불가입니다. 엔론이 FERC 명령에 대한 답변 초안을 준비했고 답변 기한이 7월 19일이었다는 기록은 있지만, 명령의 내용이나 질문의 조정 지시와의 연관성은 제시되지 않습니다. [Data: Reports (950, 2437, 2778, 2026, 2385)]
>
> **9월 — 조정 판사의 권고:** 확인되는 내용은 Judge Young이 Business Plan을 실행 가능한 청사진으로 평가하고, 세 ISO가 사용하는 기술에 대한 독립 평가와 시장 설계의 신중한 검토, 거버넌스 및 이해관계자 절차에 관한 지침을 권고했다는 것입니다. 따라서 이 권고에서 확인되는 기술적 쟁점은 세 ISO의 기술이었고, 시장 설계와 거버넌스는 추가 검토 대상으로 다뤄졌습니다. 다만 해당 권고가 9월에 이루어졌다는 날짜는 보고서에서 확인되지 않습니다. [Data: Reports (2530)]
>
> 결론적으로, 확인 가능한 차이는 Judge Young의 권고가 **세 ISO의 기술 평가와 시장 설계·거버넌스의 추가 검토**를 다뤘다는 점뿐입니다. 이를 엔론의 5월 제안이나 FERC의 7월 조치와 비교하거나, 세 단계에서 통합 기반·시장 설계의 주체가 어떻게 바뀌었는지 판단할 근거는 부족합니다. [Data: Reports (2530, 2542, 2437, 2778, 2026, +more)]

**응답이 인용한 보고서** (목록 일부 생략: +more)

- 2520 · L2 · Southeast RTO and FERC Grid Reorganization
- 2437 · L2 · EPMI and FERC Energy-Market Operations
- 2778 · L2 · RTO Stakeholder Advisory Committees and Enron Recipients
- 2026 · L2 · Seabrom Adamson, Tabors, and the RTO Study
- 2833 · L2 · NERC Governance, Standards and Security
- 2542 · L2 · NYISO, Enron, and Northeast Electricity Market Reforms
- 950 · L2 · Seabron Adamson, Frontier Economics, and Enron RTO Work
- 2385 · L2 · Hebert and FERC Energy-Market Regulation
- 2530 · L2 · FERC, RTO Week, and Electricity Market Policy

**정답 (채점 기준)**

> 5월 엔론은 PJM·뉴욕·뉴잉글랜드를 PJM 시장 설계에 기초한 단일 RTO로 통합하자고 요청했다. 7월 FERC는 PJM을 통합 기반으로 조건부 승인하고 뉴욕·뉴잉글랜드의 개별 제안은 거절했으며 세 계통운영기관에 조정 참여를 지시했다. 9월 조정 판사는 뉴욕·뉴잉글랜드 계통운영기관이 공동 제안한 시장 설계를 권고했다.

원문 근거 번호(연간 CSV): 2428, 4018, 5452

## Q26 · SEC 조사 대응과 정보 공개

*추세 · 응답 · 71초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 86개*

**질문**

> 10월 엔론은 SEC의 정보 요청에 대해 공개적으로 어떤 입장을 밝혔고, 직원에게 어떻게 대응하라고 안내했나? 11월 재무제표 재작성 공지에서는 어떤 경로로 어떤 재무 정보를 추가 공개했다고 알렸나?

**응답**

> ### 10월: SEC 정보 요청에 대한 입장과 직원 안내
>
> 2001년 10월 22일, 엔론은 보도자료를 통해 SEC의 정보 요청 사실을 알리고 조사에 협조하겠다고 밝혔습니다. 동시에 사안의 법적 성격을 이유로 논평을 제한했습니다. [Data: Reports (609, 3524)]
>
> 직원 대응과 관련해서는, 10월 29일자 이메일이 SEC 조사에 대해 논평하지 말고 해당되는 동료들에게 이메일을 전달하라고 안내한 기록이 있습니다. 다만 직원들이 SEC 문의에 답할 때 사용할 구체적인 문구나 절차까지 정해졌는지는 확인 불가입니다. 별도로 케네스 레이는 직원들에게 문제가 된 파트너십이 이미 검토·승인됐다고 설명한 것으로 기록되어 있으나, 이것이 구체적인 문의 대응 지침을 뜻하는지는 확인되지 않습니다. [Data: Reports (886, 1017, 484)]
>
> ### 11월: 재작성 공지와 추가 재무정보
>
> 11월 8일 엔론은 관련자 거래 및 부외거래에 관한 추가 정보를 SEC 제출 Form 8-K를 통해 제공했다고 밝혔습니다. 다만 그 보고서는 추가 정보의 구체적인 내용이나 금액을 제시하지 않으며, 해당 Form 8-K가 재무제표 재작성 공지 자체였다고 명시하지도 않습니다. [Data: Reports (986)]
>
> 재작성과 관련해 확인되는 내용으로는 1997~2000년 및 2001년 1·2분기 재무제표를 재작성할 계획과, JEDI·Chewco를 1997년 11월부터 소급 연결하고 LJM 관련 연결 및 감사 조정·재분류를 반영한다는 설명이 있습니다. 별도 기록은 약 4년 반치 실적 재작성으로 종전 보고 이익이 5억 달러 넘게 줄었으며, 3분기 손실과 주주자본 12억 달러 감소도 보고됐다고 설명합니다. 그러나 이 자료들은 재작성 공지의 구체적인 전달 경로를 확정해 주지 않습니다. [Data: Reports (139, 105, 2195)]
>
> 또한 3분기 10-Q에는 최대 6억 9천만 달러의 지급 가능성과 재무상 위험에 대한 경고가 담겼고, 투자자 콘퍼런스콜 녹취록을 SEC에 제출하고 회사 웹사이트에 게시할 계획이라는 기록이 있습니다. 녹취록 게시 계획의 실제 이행 여부는 확인 불가이며, 이 내용이 재작성 공지에 포함됐다고 자료가 연결해 주지도 않습니다. 따라서 **11월 재작성 공지에서 어떤 경로로 어떤 추가 재무정보를 알렸는지는, 위와 같이 별도로 기록된 공시와 구분하면 확인 불가**입니다. [Data: Reports (2247, 351)]

**응답이 인용한 보고서**

- 609 · L1 · SEC–Enron Inquiry and Oversight Network
- 3524 · L2 · Enron SEC Inquiry and Press Release
- 886 · L2 · Karen Denne, Enron Communications, and California Energy Outreach
- 1017 · L2 · Enron SEC Information Request
- 484 · L1 · Enron, Kenneth Lay, and the Bush Administration
- 986 · L2 · Enron Transaction Information Release and Form 8-K
- 139 · L1 · Enron Financial Restatement: JEDI, Chewco, and LJM
- 105 · L1 · Enron and Its Government Affairs Network
- 2195 · L2 · Enron Corp.: Energy Markets, Oversight, and Financial Crisis
- 2247 · L2 · SEC Oversight of Enron and Financial Disclosures
- 351 · L1 · SEC Oversight of Enron, Arthur Andersen, and Corporate Accounting

**정답 (채점 기준)**

> 10월에는 보도자료를 내고 SEC 요청과 협조 방침을 알렸다. 직원에게는 내부 Q&A와 설명회를 안내하면서 SEC 조사에 대해 언급하지 말라고 했다. 11월 8일에는 회사 웹사이트와 SEC에 제출한 Form 8-K에서 특수관계자·부외거래, 주주지분 감소, 연결회계와 재무제표 재작성, 이사회 특별위원회에 관한 정보를 공개했다고 알렸다.

원문 근거 번호(연간 CSV): 6567, 6608, 7192, 7506

## Q27 · 퇴직급여 검토와 인력 감축 후 지원

*추세 · 응답 · 90초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 158개*

**질문**

> 11월 후반 엔론은 직원 감축에 대비해 퇴직급여와 안내 방식을 어떻게 검토했나? 12월 초 감축 뒤에는 남은 조직에서 HR 문의와 비상 연락을 어떻게 이어가려 했나?

**응답**

> ### 11월 후반: 퇴직급여와 직원 안내 검토
>
> 11월 20일로 예정된 Enron–Dynegy 회의 안건에는 인원 감축·구조조정·직원 유지와 함께 퇴직급여가 포함됐다. Oxley는 근속연수당 2주분에 급여에 따른 추가분을 더하는 방안의 계산을 확인해 달라고 요청했고, 약 3,500만 달러와 4,500만 달러로 추산한 대안도 검토됐다. 이는 제안과 예정된 논의이며, 어떤 안이 채택되거나 실제 지급됐다는 기록은 없다. 퇴직급여 변경이 직원에게 알려야 할 복리후생 변경인지도 제기됐고, Oxley는 회의 자료에 대한 법무팀 검토를 요청했으나 최종 공지 방침은 확인되지 않는다. [Data: Reports (140, 1130)]
>
> 직원 안내 방식과 관련해서는 NETCO 공지의 내용과 소통 방식을 검토하도록 요청한 기록이 있으며, 일부 수신자는 직원 유지 프로그램이 마련된 뒤 공지하는 방안을 선호했다. 다만 이는 검토·의견 단계로, 확정된 안내 일정이나 방식은 확인되지 않는다. 별도의 감축 계획 기록에는 표준 퇴직급여 적용과 HR의 안내 조언, 추가 급여의 승인 대기 내용이 있으나, 이를 11월 후반의 검토로 특정할 근거는 없다. [Data: Reports (1130, 2032)]
>
> ### 12월 초: 감축 이후의 HR 문의와 비상 연락
>
> 한 보고서는 Enron의 운영 축소 과정에서 최근 이틀간 감축이 있었고 HR 인력도 추가로 줄어들 수 있다고 기록한다. 그러나 남은 조직에서 HR 문의를 누가 맡고 어떤 절차나 연락처로 처리하려 했는지는 제시하지 않는다. [Data: Reports (1197)]
>
> 직원 우려를 제기할 별도 창구로 Employee Relations를 두고 Cindy Olson이 이끌도록 한 조직 계획은 확인되지만, 감축 이후 이 창구가 실제로 유지·운영됐는지는 알 수 없다. 비상 연락의 경우 Randy Lord가 2001년 5월 시설 비상 연락 목록을 수정·배포한 별도 기록이 있으나, 이것이 12월 감축 이후의 연락 체계로 이어졌다는 근거는 없다. 따라서 감축 이후 HR 문의와 비상 연락을 유지하려 한 구체적인 담당자·절차·계획은 **확인 불가**다. [Data: Reports (1042, 1141)]

**응답이 인용한 보고서**

- 140 · L1 · Enron Human Resources and Workforce Governance
- 1130 · L2 · David Oxley, Enron HR, and Dynegy Planning
- 2032 · L2 · Ann Hill, Jo Ann, and Enron HR Restructuring
- 1197 · L2 · Enron Leadership, Surveys, and Employee Communications
- 1042 · L2 · Enron Office of the Chairman and Related Staff
- 1141 · L2 · Enron Facilities, Emergency Preparedness, and Property Initiatives

**정답 (채점 기준)**

> 11월에는 근속기간·급여에 따른 퇴직급여 산식과 시나리오별 비용을 검토했고, 다른 복지 변경과 별도로 공지하는 방식을 논의했다. 12월 감축 뒤에는 중앙 HR 전문 지원팀을 두고 새 담당자 명단을 공유했다. 시설 비상 연락망의 부서별 연락처도 갱신하도록 요청했다.

원문 근거 번호(연간 CSV): 7855, 7896, 8083, 8214, 8220

## Q28 · NEPOOL 재무보증과 선납 협상

*추세 · 응답 · 59초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 29개*

**질문**

> 11월 말 엔론은 NEPOOL의 재무보증 요건을 어떤 방식으로 충족하고 있다고 설명했나? 12월에는 기존 보증에 어떤 문제가 생겼고, 기존 거래를 이어가기 위해 어떤 납부 방식을 협상했나?

**응답**

> 11월 말, EPMI와 EES는 Enron Corp.의 보증에 의존하지 않고 NEPOOL 재무보증 요건을 충족하기 위해 **6,000만 달러를 초과하는 보증채권을 게시하고 있다**고 설명했다. [Data: Reports (2438, 384)]
>
> 12월에는 보증채권이 취소되어 NEPOOL에서 잠재적인 신용경색 우려가 생겼다. 별도로 ISO New England는 EES가 재무보증 요건을 이행하지 못했다고 통지하고 12월 21일까지 시정하도록 요구했다. Safeco도 파산 절차 이후 Enron에 대한 보증신용을 연장하지 않겠다고 통보했다. [Data: Reports (2438, 384, 214)]
>
> 기존의 수익 상태(in-the-money) 거래를 계속 이행할 수 있도록 Enron 측은 ISO-NE 및 NEPOOL과 재무보증 정책 적용을 일정 기간 유예하는 방안을 협상했다. 또한 EPMI, EES, EEMC가 12월 27일부터 에너지 및 기타 NEPOOL 서비스 비용을 3일 단위로 선납하는 안이 제안됐다. NEPOOL이 비용을 추산하고 영업일마다 송금한 뒤 매월 정산하는 방식이었다. 다만 이 선납안의 최종 시행 여부는 확인되지 않는다. 에스크로에 자금을 예치하는 방안도 계획됐으나 최종 승인을 기다리는 상태였다. [Data: Reports (2438, 384)]

**응답이 인용한 보고서**

- 2438 · L2 · NEPOOL, ISO-NE, and FERC Market Governance
- 384 · L1 · Enron EPMI, FERC, and NEPOOL Power Markets
- 214 · L1 · Enron Energy Companies and ISO New England

**정답 (채점 기준)**

> 11월 말 내부 메일은 EPMI와 EES가 모회사 보증에 의존하지 않고 6,000만 달러를 넘는 보증증권을 제출해 요건을 충족한 것으로 파악했다고 설명했다. 12월에는 보증업체들이 보증증권을 취소했고 ISO New England는 EES에 재무보증 요건 미충족을 통보했다. 엔론은 기존 거래 이행을 위해 EPMI·EES·EEMC가 NEPOOL의 전력과 서비스 비용을 최소 3일치가 유지되도록 선납하는 방안을 협상했고, 그 기본 조건을 FERC에 제출했다고 보고했다.

원문 근거 번호(연간 CSV): 8120, 8324, 8373, 8399

## Q29 · 교토의정서 이행과 배출권거래

*추세 · 응답 · 68초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 89개*

**질문**

> 5월 덴마크 의회의 조치부터 7월 본(Bonn) 회의와 10월 유럽위원회의 배출권거래제 초안까지, 교토의정서 비준 준비와 시장 규칙은 어떻게 구체화됐나? 본 회의에서 시장 기반 수단의 사용량에 정량적 상한을 두기로 했는지와 유럽위원회 초안이 단계별로 어떤 온실가스를 다루려 했는지를 설명하라.

**응답**

> ### 시기별 구체화
>
> **5월 덴마크 의회:** 5월 29일 덴마크 의회는 덴마크가 교토의정서의 EU 공동 비준 절차에 참여하도록 하는 결의안을 88대 9로 승인했다. 에너지 장관 스벤 아우켄은 의정서와 기후협상을 계속하는 데 지지를 표했다. 다만 이 결의가 덴마크의 국내 비준 완료나 이후 이행 확정을 뜻하지는 않는다. [Data: Reports (2717)]
>
> **7월 본(Bonn) 회의:** 본에서 국제 협상이 재개됐고, 178개국 대표가 교토의정서 이행 규칙에 합의했다는 기록이 있다. 그러나 합의된 규칙의 세부 내용은 충분히 제시되어 있지 않으며, 배출권거래·청정개발체제(CDM)·공동이행(JI) 등 시장 기반 수단의 사용량에 **정량적 상한을 두기로 했는지는 확인 불가**다. [Data: Reports (3290, 556, 2996)]
>
> **유럽위원회 배출권거래제 초안:** 2001년 10월 단계에서 유럽위원회가 기후변화 패키지의 일부로 초안을 제시했다는 보고가 있다. 다만 다른 기록은 초안의 구체적인 발표일을 제시하지 않아 10월 발표 여부를 확정하기는 어렵다. 초안은 제안·계획이며, 채택되거나 실제 시행됐다는 뜻은 아니다. [Data: Reports (565, 3365)]
>
> 초안의 계획상 1단계는 2005~2007년, 2단계는 2008~2012년이었다. 1단계에는 회원국이 배출권 이월을 제한할 가능성과 비EU 국가 프로그램과의 연계 검토가 포함됐다. 2단계에는 할당 규칙을 조화하고 온실가스 적용 범위를 확대할 계획이었다. 그러나 각 단계에서 다루려던 **온실가스의 구체적인 종류는 확인 불가**다. 따라서 자료로 확인되는 것은 시장 규칙의 단계 구분과 일부 계획된 제도 방향이며, 대상 가스 목록이나 본 회의의 정량적 상한이 유럽위원회 초안에 반영됐는지는 확인할 수 없다. [Data: Reports (3365, 565)]

**응답이 인용한 보고서**

- 2717 · L2 · Denmark, Wind Energy, and Kyoto Policy
- 3290 · L2 · Bonn Climate Negotiations and Kyoto Rules Agreement
- 556 · L1 · Germany’s Energy Market: E.ON, RWE, and Gas Access
- 2996 · L2 · Kyoto Protocol, Bonn Agreement, and U.S. Climate Policy
- 565 · L1 · European Commission, EU Energy Markets, and EDF
- 3365 · L2 · EU Climate Change Package and Emissions Trading Directive

**정답 (채점 기준)**

> 5월 덴마크 의회는 다른 EU 회원국과 함께 교토의정서를 비준할 수 있도록 승인했다. 7월 본 회의에서는 배출권거래 등 시장 기반 수단의 사용량에 정량적 상한을 두지 않기로 정치적 합의를 이뤘다. 10월 유럽위원회는 EU 비준을 위한 문서와 배출권거래제 지침 초안을 기후 패키지에 담았다. 초안은 1단계(2005~2007년)에 CO₂만을 대상으로 하고 2단계(2008~2012년)에 모든 온실가스로 확대하자는 내용이었다.

원문 근거 번호(연간 CSV): 3064, 4463, 6787

## Q30 · 다볼 발전사업 협상

*추세 · 응답 · 78초 · 읽은 보고서 4,036개 · 묶음 276개 · 점수 붙은 핵심 문장 183개*

**질문**

> 4월 다볼 발전회사가 마하라슈트라 주정부에 보낸 중재 통지의 쟁점은 무엇이었나? 7월 켄 레이가 희망한 인수 주체와 11월 매각 자문보고서가 자금 조달을 검토한 후보는 각각 누구였나? 11월에 검토한 이전 통지를 보내면 어떤 절차가 시작되는지도 설명하라.

**응답**

> ### 4월 중재 통지
>
> 다볼 발전회사(DPC)는 마하라슈트라 주정부가 주정부 지원협정상의 의무를 이행하지 않았다고 주장하며 중재를 통지한 것으로 보고되어 있다. 중재에서 다룰 쟁점은 그 의무 위반 여부였으며, 이는 DPC의 주장이었지 위반이 확정된 판정은 아니다. 배경에는 MSEB의 미지급 전력대금 약 4,500만 달러가 있었지만, 자료만으로 이 금액이 통지의 구체적인 청구 항목이었다고 단정할 수는 없다. [Data: Reports (418, 2669, 433, 2736)]
>
> ### 7월 인수 희망 주체와 11월 자금 조달 후보
>
> 7월 켄 레이가 희망한 인수 주체는 **확인 불가**다. 타타가 다볼 지분 인수와 관련해 탐색적 논의에 참여했다는 보고는 있으나, 타타가 켄 레이가 희망한 인수자였다고 확인되지는 않는다. [Data: Reports (418, 2669, 2663)]
>
> 11월 매각 자문보고서가 자금 조달을 검토한 후보도 **확인 불가**다. 인도 금융기관들이 다볼 지분 매입 협상에 관여했다는 별도 보고는 있지만, 이들이 해당 자문보고서의 검토 후보였다는 근거는 없다. [Data: Reports (414, 418, 2669)]
>
> ### 11월 검토된 통지의 절차적 효과
>
> 보고서에 따르면 DPC 이사회가 승인한 예비 해지 통지는 계약 해지와 프로젝트 포기를 위한 3단계 절차의 첫 단계였다. 통지 후 당사자들에게 11월까지 협상 기회를 주고 합의를 모색한 뒤, DPC가 계약을 해지할 수 있는 것으로 설명되어 있다. 다만 나머지 단계의 세부 내용이나 실제 통지 발송 및 최종 해지 여부는 확인되지 않는다. 한편 다른 보고서는 통지를 통해 DPC 지분 등의 가치를 산정하는 이전·매각 절차가 시작될 수 있다고 설명하지만, 이것이 앞서 말한 예비 해지 통지와 같은 통지인지는 분명하지 않다. [Data: Reports (2684, 2669, 418)]

**응답이 인용한 보고서**

- 418 · L1 · Dabhol Power Project: Enron, DPC, and MSEB
- 2669 · L2 · Dabhol Power Company, Enron, and the Maharashtra Dispute
- 433 · L1 · Enron–Dabhol Dispute: Maharashtra and IDBI
- 2736 · L2 · Enron India, MSEB, and the Dabhol Dispute
- 2663 · L2 · Tata Power: Q2 Earnings and Dabhol Stake Negotiations
- 414 · L1 · Enron India, Dabhol and the Lender Dispute
- 2684 · L2 · Dabhol Power Dispute: DPC, MSEB and Lenders

**정답 (채점 기준)**

> 4월에는 마하라슈트라 주정부의 지원약정 불이행을 두고 중재 개시를 통지했다. 7월에는 켄 레이가 인도 중앙정부의 다볼 지분 인수를 희망한다고 한 발언이 보도돼 대외 답변을 준비했다. 11월 초에는 가치평가 절차를 시작하는 이전 통지를 보낼지와 시기를 검토했다. 11월 중순에는 자문 보고서가 잠재적 인수 주체인 Tata의 인수자금 조달을 검토했다고 전했다.

원문 근거 번호(연간 CSV): 1738, 4472, 7331, 7615

