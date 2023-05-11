# sol1. 현재 칸을 큐에 적재, 같은 크기의 true/false 맵에 현재위치 true 
# -> 바라보는 방향의 공간이 0인지 확인후 0일때 전진, 전진한 위치의 값을 true로 변환 
# -> 빈칸(0)이 모두 true일 때 주변에 양옆에 청소되지 않은 칸이 나올 때 까지 후진(바라보는 방향의 반대로 이동) 
# -> 후진 할 수 없을 때 종료(값 반환)
# gg 1회차 포기 (1시간 36분)

n,m = map(int, input().split())
r,c,way = map(int, input().split())
room = []*n
for i in range(n):
    room.append((input().split()))

# 청소확인용 청소됐을때 1로 변환
check = room
cnt = 1

# 이동에 관여하는 변수 필요
# 3*3 크기로 중심을 기준으로 동서남북 한칸씩 이동 가능
def straight(r,c,w):
    if w == 0: return r-1,c
    elif w == 1: return r,c-1
    elif w == 2: return r+1,c
    elif w == 3: return r,c+1

def back(r,c,w):
    if w == 0: return r+1,c
    elif w == 1: return r,c+1
    elif w == 2: return r-1,c
    elif w == 3: return r,c-1

def checkWay(r,c,w):
    if w==0 and room[r-1][c] == 0: return w
    else: 
        return 1
    if w==1 and room[r][c-1] == 0: return w
    else: 
        return 2
    if w==2 and room[r+1][c] == 0: return w
    else: 
        return 3
    if w==3 and room[r][c+1] == 0: return w
    else: 
        return 0

while True:
    # 칸이 비어있고 청소가 되지 않았을 때
    if check[r-1][c] == 0 and room[r-1][c] == 0:
        w = checkWay(r, c, w)
        straight(r, c, w)
        cnt+=1
    if check[r][c-1] == 0 and room[r][c-1] == 0:
        w = checkWay(r, c, w)
        straight(r, c, w)
        cnt+=1
    if check[r+1][c] == 0 and room[r+1][c] == 0:
        w = checkWay(r, c, w)
        straight(r, c, w)
        cnt+=1
    if check[r][c+1] == 0 and room[r][c+1] == 0:
        w = checkWay(r, c, w)
        straight(r, c, w)
        cnt+=1
    # 칸은 비어있지만 청소가 되었을 때
    if check[r-1][c] == 1 and room[r-1][c]==0:
        back(r, c, w)
    if check[r][c-1] == 1 and room[r][c-1]==0:
        back(r, c, w)
    if check[r+1][c] == 1 and room[r+1][c]==0:
        back(r, c, w)
    if check[r][c+1] == 1 and room[r][c+1]==0:
        back(r, c, w)


check[r][c] = 1

