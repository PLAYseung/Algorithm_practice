
## [기지국 설치](https://school.programmers.co.kr/learn/courses/10302/lessons/62946)

- n개의 아파트 중에 4G 기지국이 설치된 아파트는 5G 기지국으로 교체하고
    신호가 다이지 않는 곳 까지 다을 수 있게끔 기지굴 추가 설치할 때 최소로 설치할 수 있는 갯수

## 요소

- 입력 : 
  - N : 아파트의 갯수
  - station : 기지국의 위치
  - W : 5G 전파의 범위

- 출력 : 추가 설치해야 하는 기지국의 갯수

## result

- [처음 문제 풀이](/src/Solution.java)
<br/> 기존에 설치한 기지국 위치에 설치 하고 범위를 마킹
<br/> 처음 부터 마킹한 자리를 제외한 부분 중에서 범위의 중간을 마킹
<br/> 마킹이 다 채워질때 까지 반복 - X

- [두번째 문제 풀이](/src/sndSolution.java)
<br/> answer : 추가 설치해야 하는 기지국
<br/> si : stations를 하나씩 훑어서 지나갈 포인터
<br/> position : 기지국이 설치된 아파트
<br/> position의 값은 첫번째 부터 대역폭 만큼 서치 하면서 올라온 값
<br/> stations의 값을 꺼내서 positon(적용되는 대역폭)안에 있을 때 넘어가기 위한 조건을 줌
