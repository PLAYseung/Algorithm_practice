# [가장 큰 수](https://school.programmers.co.kr/learn/courses/10302/lessons/62948)

0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수?

# 요소

- 입력 : 0 또는 양의 정수로 이루어진 리스트

- 출력 : 가장 큰 수를 문자로 리턴

# result

- [문자로 순서를 정렬](/src/main/java/org/fstSolution.java)
<br/> 입력받은 리스트의 숫자들을 문자로 변환해서 큰 순서대로 조합
<br/> 첫번째 테스트 통과 두번째 테스트 실패
<br/> 두번째 테스트 중 34 30 3 순서로 정렬됨

- [정렬시 버블 정렬 활용](/src/main/java/org/sndSolution.java)
<br/> 정렬시 버블 정렬로 값들을 정렬
<br/> 정렬할 때 순서를 바꿨을 때의 값을 비교 하여서 정렬에 반영

- [자바의 라이브러리 활요](/src/main/java/org/trdSolution.java)
<br/> 자바의 라이브러리를 최대한 활용하여 문제 풀이
<br/> 단계별로 줄이는 형태가 남겨져있음