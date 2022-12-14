
## [문자열 압축](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

- 두개의 큐 리스트 각각의 합이 같게 하고 큐에서 insert와 pop을 묶어서 1회 이라고 간주함
- 가장 적게 이동해서 같은 값을 만들것
- 두 큐의 값이 같을 수 없으면 -1을 반환


## 요소

- 입력 : queue1, queue2 ; 두개의 큐는 길이가 같다

- 출력 : solution -> result


## 예상도

1. 두 리스트의 합이 홀수인지 짝수인지 비교 : 
    - 통과 할수 없는 조건
        - 홀수이면 -1 반환
        - 두 리스트 모두 홀수만 가지고 있으면 합은 짝수 이지만 나눌수 없을 수도 있다 [1,3] [3,3]
        - 두 리스트에 모두 짝수 여도 나눌수 없는 경우도 존재한다 [2,2] [8,2]

    - 통과 조건
        - 두 리스트의 합이 짝수
        - 두 리스트 중에
        - 두 리스트 모두 같은 홀수 값을 가지고 있다면 나눌수 인수가 홀수이지만 두개로 나눌 수있다 [3,3,3] [3,3,3]

    - ?
        - X :정렬 후 앞에서부터 값을 더해가면서 뒤에 있는 값들과 비교 
                [1,1,1,1,2,2,2,10] -> 10 : 10
                [2,4,4,6] -> 6 : 10 -> 12 : 6

        -단순히 생각하면 (두 리스트가 값이 같을때; 종료조건) 종료   --> -1 반환은 어떻게?
            - -1을 반환하려면 초기에 걸러 내야함
            - 반복 조건을 for문 사용해서 원래 인덱스 길이의 두배 이상 돌아도 끝나지 않을 경우 -1 반환



2. 두 리스트의 값 비교 : 일치하면 횟수 반환

3. 두 리스트에서 pop & insert 한 이후 횟수 1 증가
    조건)   pop은 0번째 인덱스만 가능
            insert는 리스트의 가장 뒤에만 가능

## result

- sum 연산을 매번 반복하지 않도록 해서 시간 복잡도를 줄일 것
- deque의 자료구조 이용

