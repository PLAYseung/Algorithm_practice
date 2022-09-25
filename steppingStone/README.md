## [징검다리 건너기](https://school.programmers.co.kr/learn/courses/30/lessons/64062)

- 징검다리는 한번 밟을 때 마다 숫자가 1 줄어든다
- 디딤돌이 0이 되면 더 이상 밟을 수 없다
- 다음으로 밟을 수 있는 디딤돌이 여러개일 경우 가장 가까운 디딤돌로 건너뛸수 있음
- k 칸 씩 건널 수 있다
- 최대 몇명 까지 건널 수 있는지
- 징검다리를 건널 수 있는 수는 무제한
- stones 1 ~ 200,000
- 각 원소들의 값 1 ~ 200,000,000
- k 는 1 이상 자연수

## 요소

- 입력 : <br/>  
        stones  : list<br/>
        k       : 건널수 있는 최대 거리 ( k=3; 1 번 -> 4번 )

- 출력 : solution -> result


## 예상도

- 0인 디딤돌이 k번 나오면 건널수 없음
    + 리스트를 0번 부터 끝까지 훑어서 보면 되는가?
- 배열의 원소들의 크기는 1 ~ 200,000,000 사이 <br/>  
    cross          : 건널 수 있는 사람의 수  <br/>  
    left, right    : 최대 인원수를 찾기위한 변수  <br/>
    t - cross      : 돌이 최대로 지나가게 할 수 있는 인원수가 얼마나 연속하는지 알기 위함


## result

- 정화도 테스트 통과, 효율성 테스트 실패(시간 초과)
    + [code](/steppingStone/steppingstone_acc.py)
- 효율성 테스트 통과
    + [code](/steppingStone/steppingstone_eff.py)
