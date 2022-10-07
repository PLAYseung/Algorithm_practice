# [예산](https://school.programmers.co.kr/learn/courses/10302/lessons/62949)

1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다
<br/>상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정합니다.

# 요소
- 입력 : 
<br/>　　budgets : 지역별 필요한 예산 
<br/>　　M : 전체 예산

- 출력 : 상한액

# result
- [M을 리스트의 갯수로 나눔](/app/src/main/java/budget/fstSolution.java)
<br/> M을 리스트의 갯수로 나눠서 내림한 값을 출력
<br/> 입출력 예시, 테스트 케이스 1개 통과

- [M을 리스트의 갯수로 나눔](/app/src/main/java/budget/sndSolution.java)
<br/> 첫번째 문제 풀이 방식에 while문을 결합해서 예산을 최소한으로 남기기
<br/> 입출력 예시, 테스트 케이스 1개 통과
<br/> 반복 횟수의 문제가 아닌듯 해보임

- [max min 값을 비교](/app/src/main/java/budget/trdSolution.java)
<br/> max 값과 min 값의 중간 값을 이용 
<br/> 전체 예산의 합이 M값 이상일 때
<br/> min 값과 mid 값의 차이만큼을 최대 값에 배분 하면서 차이를 줄여 나감
<br/> [IntStream을 활용한 코드 줄이기](/app/src/main/java/budget/cleancode.java)