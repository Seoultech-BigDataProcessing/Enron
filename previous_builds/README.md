# 이전 구축

본 그래프(`enron/`)를 만들기 전에 한 구축들이다. **실험에는 쓰지 않는다.** 비교와 기록용이다.

| 폴더 | 메일 | 내용 |
|---|---|---|
| `1_test_500mails_all_recipients/` | 500통 | 첫 사전 테스트. 받는 사람을 전부 넣었더니 "메일을 받았다"는 관계가 40%를 차지했다 |
| `2_test_500mails_max5_recipients/` | 500통 | 두 번째 사전 테스트. 받는 사람을 5명까지만 넣어 위 문제를 줄였다. 본 구축은 이 방식을 쓴다 |
| `3_first_half_3661mails/` | 3,661통 | 2001년 상반기만으로 한 구축. 이후 하반기를 더해 본 그래프를 만들었다 |

각 폴더의 `output/`은 graphrag 구축 결과, `logs/`는 구축 로그, `input/`은 구축에 쓴 메일이다.
1번의 입력은 따로 남기지 않았다.

- 사전 테스트의 자세한 내용: [docs/trial_500.md](../docs/trial_500.md)
- 본 구축 결과: [docs/main_build.md](../docs/main_build.md)

이 그래프에 질문하려면 설정은 `enron/`의 것을 쓰고 `--data`로 결과 폴더를 지정한다.

```
graphrag query --root ./enron --data ./previous_builds/3_first_half_3661mails/output --method global "질문"
```
