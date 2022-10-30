# [게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/10302/lessons/62951)

<br/> n과 m의 크기는 1이상 100 이하
<br/> n과 m이 모두 1인 경우는 없다
<br/> 출발지는 (0,0) 이고 도착지는 (n,m)이다
<br/> 0이 벽이고 1이 길이다
<br/> 목적지에 갈 수 있는 방법이 없으면 -1을 반환한다
<br/> 목적지에 갈 수 있는 최소한의 칸을 정답으로 반환한다

# 요소

- 입력 : [0과 1로 이루어진] n X m 행렬

- 출력 : 제일 짧은 경로

# result

- [해당 위치에서 진행 가능한 길의 갯수 이용](/GameMap/src/fthsolution.java)
<br/> 캐릭터가 4방향중 진행 가능한 방향에 대한 갯수를 정의
<br/> 처음과 끝의 갯수를 뺀 나머지를 모두 더함

- [BFS에 대한 이해 필요](/GameMap/src/BFS.java)
<br/> 그래프 탐색 : 어떤것들이 연속해서 이어질때, 모두 확인하는 방법 [vertex(노드) + edge(간선)]
<br/> BFS(너비 우선 탐색) : 가지고 있는 자식 노드를 저장 레벨별로 진행 -> Queue
<br/> DFS(깊이 우선 탐색) : 가지고 있는 자식 노드의 끝까지 갔다가 돌아오기 -> Stack

- [BFS에 대한 이해 필요](/GameMap/src/sndsolution.java)
<br/> Queue를 이용한 BFS 알고리즘에 대한 진행 방식
<br/> 모든 구간을 탐색하는 것이 아닌 갈 수 있는 구간을 탐색 후
<br/> 다음 탐색을 진행하는 형식