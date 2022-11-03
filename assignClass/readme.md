
## [강의실 배정](https://softeer.ai/practice/info.do?idx=1&eid=392)

<br/> 배정된 강의는 서로 겹치면 안됨
<br/> 수업시간의 길이와 상관 없이 최대한 많이 배정
<br/> 두 강의의 시작시간과 종료시간은 겹쳐도 됨

## 요소

- 입력 : 
    * 강의 개수 N
    * 강의시작 강의종료 : S1 F1
    * 강의시작 강의종료 : S2 F2

- 출력 : 최대 강의의 수

## result

- [종료 시간과 시작 시간을 비교](/assignClass/assignClass.py)
    <br/>ㅤㅤㅤㅤㅤㅤheapq
    <br/>ㅤㅤㅤㅤㅤㅤheappush : 입력의 기준 값으로 정렬
    <br/>ㅤㅤㅤㅤㅤㅤheappop : 기준 값이 가장 작은 리스트(튜플)를 삭제하고 반환