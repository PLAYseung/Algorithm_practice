# [숫자 게임](https://school.programmers.co.kr/learn/courses/10302/lessons/62947)

- A와 B는 값이 정해져있다
- B는 A가 어떤 값을 낼지 알고 있기 때문에 B가 원하는 값을 원하는 때에 낼수 있다
- B가 최대로 이길 수 있는 횟수는?

# 요소

- 입력 : 길이가 같은 두 리스트 A, B

- 출력 : B가 A를 가장 많이 이기는 경우의 승리 횟수

# result

- [두 리스트를 정렬 후 비교](/numberGame_java//src/fstsolution.java)
<br/> 두 리스트를 각각 정렬 후 
<br/> A에 대한 B값을 비교하고 A값의 마지막에 결과를 반환
<br/> 파이썬으로 풀었던 경험이 있던 문제
<br/> -전체 테스트 통과 / 효율성 검사 오류 발생

- [반복문 1회 사용](/numberGame_java/src/sndsolution.java)
<br/> A 리스트만 정렬 후 처음부터 뒤로 가면서 비교
<br/> 효율성 테스트에서 실패
<br/> 두 리스트 각각 정렬 후
<br/> 큰 수부터 하나씩 내려가면서 비교
<br/> [효율성 테스트 통과](/numberGame_java/src/trdsolution.java)