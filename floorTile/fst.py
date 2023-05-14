# sol1. (0,0)부터 순차적으로 진행
# 모양에 따라 행, 열을 확인
# 같은 모양의 타일이 나오지 않을 때 까지 전진
# 전진해서 방문한 곳은 방문처리
# (n-1.m-1)에서 종료
# 반복한 횟수만큼을 출력

n,m = map(int, input().split())
room = []
checked = [[False]*(m) for _ in range(n)]
cnt = 0


for i in range(n):
    room.append(list(input()))

def sol(y,x,p):
    global checked, cnt

    # 모양에 대해서만 구분
    if p == '|':
        # 열의 방향으로만 이동하기 때문에 y+1
        y += 1
        # y값이 인덱스를 초과할 때
        if y == n:
            return
        # 다음에 오는 모양이 다를때
        if room[y][x] == '-':
            return
    elif p == '-':
        # 열의 방향으로만 이동하기 때문에 x+1
        x += 1
        # x값이 인덱스를 초과할 때
        if x == m:
            return
        # 다음에 오는 모양이 다를때
        if room[y][x] == '|':
            return

    # 연결되는 동안은 반복 호출
    sol(y, x, p)
    # 연속되는 곳 방문처리
    checked[y][x] = True


for i in range(n):
    for j in range(m):
        if not checked[i][j]:
            sol(i, j, room[i][j])
            cnt+=1

print(cnt)