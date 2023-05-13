# N x M 크기의 맵
# 반시계 방향으로 우선 돌고 시작
# 0 이동 가능한 공간 / 1 이동 불가능한 공간
# 북(0) -> 서(3) -> 남(2) -> 동(1) 순서로 회전(반시계 방향)
# 4방향에 청소할 곳이 없으면 후진한다
# 후진할 곳이 없으면 정지한다

n,m = map(int, input().split())
r,c,d = map(int, input().split())
room = []
for i in range(n):
    room.append(list(map(int, input().split())))

checked = [[False]*m for _ in range(n)]

# d = 0 일때 r-1,c
# d = 1 일때 r,c+1
# d = 2 일때 r+1,c
# d = 3 일때 r,c-1
# 0 -> 3 -> 2 -> 1

# d의 값으로 dx,dy를 호출
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 0 -> 3 이되는 방법
# (0+3)%4 = 3
# 회전을 할때 수식

# 후진할 때 
# 0 -> 2, 1 -> 3, 2 -> 0, 3 -> 1
back = [2,3,0,1]

checked[r][c] = True

cnt = 1

while 1:
    checkWay = 0
    # 각 방향에 대해서 한번씩 동작 할 수 있도록
    for _ in range(4):
        # 무조건 반시계 방향으로 90도 회전후 전진이기 때문에 회전
        d = (d+3)%4

        # 앞으로 나갈 위치의 좌표
        nr = r+dy[d]
        nc = c+dx[d]

        # 앞에 벽이 없다면
        if room[nr][nc] == 0:
            # 정소를 하지 않았다먼
            if not checked[nr][nc]:
                checked[nr][nc] = True
                # r,c를 전진한 위치의 좌표로 변경
                r = nr
                c = nc
                checkWay = 1
                cnt += 1
                # for문 종료후 다시 시작
                break
    
    # 청소를 하지 못한 경우
    if checkWay == 0:
        # 후진시 벽과 만나면 종료
        if room[r+dy[back[d]]][c+dx[back[d]]] == 1:
            break
        else:
            r +=dy[back[d]]
            c +=dx[back[d]]

print(cnt)



print(cnt)