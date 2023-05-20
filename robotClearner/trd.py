# N x M 크기의 방 
# 가장 바깥의 면은 1로 둘러 쌓여있음 1은 벽이므로 진입 할 수 없음
# 북(0) 서(3) 남(2) 동(1) 순서로 회전
# 청소를 하지 않을 경우 후진
# 후진 할 수 없을 경우 종료
# 90도 회전 -> 전진 가능 확인 -> 청소 가능 확인 

n,m = map(int,input().split())
r,c,d = map(int,input().split())

room = []

for i in range(n):
    room.append(list(map(int,input().split())))

visited = [[False]*m for _ in range(n)]

# 0[-1,0] -> 3[0,-1] -> 2[1,0] -> 1[0,1]
# (d+3)%4
x = [0,1,0,-1]
y = [-1,0,1,0]
back = [2,3,0,1]
cnt = 1
visited[r][c] = True

while 1:
    check = 0
    # 각 방향을 한번씩 확인
    for _ in range(4):
        d = (d+3)%4
        nr = r+y[d]
        nc = c+x[d]
        print(f'{nr} / {nc}')
        # 90도 회전한 방향에서 앞으로 한칸의 정보
        if room[nr][nc] == 0:
            if not visited[nr][nc]:
                r = nr
                c = nc
                visited[r][c] = True
                check = 1
                cnt += 1
                print(f'check : {r} / {c}')
                break
    
    if check == 0:
        # 후진
        if room[r+y[back[d]]][c+x[back[d]]] == 1:
            break
        else:
            r += y[back[d]]
            c += x[back[d]]

print(cnt)
print(visited)