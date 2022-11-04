import sys
from collections import deque

def solution(maps):

    # 상하좌우 비교를 위한 변수
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 최대 길이에 대한 변수를 저장
    r = len(maps)
    c = len(maps[0])

    # maps와 같은 크기의 [-1]로 차있는 리스트를 제작
    graph = [[-1 for _ in range(c)] for _ in range(r)]

    # 큐를 변수로 저장
    queue = deque()
    # 시작지점에 대한 정보를 큐에 저장
    queue.append([0,0])

    # 지나온 길이라는 정보를 남기기 위해 지나간 길에 1을 저장
    graph[0][0] = 1

    # 큐에 데이터가 있는 동안 반복
    while queue:
        # 큐의 가장 왼쪽(가장 먼저 저장된 값)을 y,x로 반환 하고 삭제
        y,x = queue.popleft()

        # y,x의 위치기준 4방향 값을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # ny와 nx가 범위 바깥으로 나가는지 확인하고 ny,nx 위치 값이 1인지 확인
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:

                # 지나오지 않은 길은 -1로 남아있다
                if graph[ny][nx] == -1:
                    # ny,nx 위치에 y,x값에 1을 더해서 저장 한다
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny,nx])

    answer = graph[-1][-1]
    return answer

    pass

def main():
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    print(solution(maps))
    pass

if __name__=='__main__':
    main()