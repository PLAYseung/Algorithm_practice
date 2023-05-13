import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
r,c,d = map(int,input().split())

# d => 0,3,2,1 순서로 돌아야한다.
# 이동할 방향(0,3,2,1)에 맞게 이동 거리를 사용하기 위함
# 서,남,동,북 순서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 처음 시작하는 곳 방문 처리
visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    # 4방향 확인
    for _ in range(4):
        # 0,3,2,1 순서 만들어주기위한 식
        # d = 0 => 3 % 4 = 3 : dx[3] r : -1 c : -
        # d = 1 => 4 % 4 = 0 : dx[0] r : -  c : -1
        # d = 2 => 5 % 4 = 1 : dx[1] r : +1 c : -
        # d = 3 => 6 % 4 = 2 : dx[2] r : -  c : +1
        # 예제 2번) d = 0 시작
        # nx = 4+0 = 4
        # ny = 7-1 = 6
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        # 한번 돌았으면 그 방향으로 작업시작
        # d = 0 부터 시작했기 때문에 시작지점에서 다음으로 접근하는 값으로 d를 변경
        # d = 3
        d = (d+3)%4
        # nx와 ny의 범위가 0~n/m 사이 이면서 graph의 [nx,ny]의 값이 0일경우 : 전진가능한 경우
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            # 방문한 적이 없는지 확인 
            if visited[nx][ny] == 0:
                # 방문한 것을 기록
                visited[nx][ny] = 1
                cnt += 1
                # 현재위치를 갱신 
                r = nx
                c = ny
                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break
    # 위의 for문에서 새롭게 방문했다면 flag=1이되어 if문을 넘어감
    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: #후진했는데 벽
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]