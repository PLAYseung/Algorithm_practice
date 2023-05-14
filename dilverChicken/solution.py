def cal():
    tmp = 0
    for hx,hy in house: # 1에 위치하는 모든 house를 하나씩 뽑아 치킨거리를 구한다
        # 10억
        dist = 1e9
        for e, (cx,cy) in t_ch: # 2에 위치한 치킨집과 특정 house와의 치킨거리를 구한다
            dist = min(dist,abs(hx - cx) + abs(hy - cy))
        tmp += dist
    # 치킨집*m개 만큼 데이터가 저장됨
    res.append(tmp)

def select_chicken(cnt):
    # 백트레킹의 조건으로 m과 숫자가 일치할 때 치킨거리를 구해 res 리스트에 저장
    if cnt == m:
        cal()
        return
    
    for e,(cx,cy) in enumerate(chick):
        if visit[cx][cy] == 0: # 특정 치킨 집을 방문했는지 처리함
            if t_ch: # 시간 단축과 오름차순의 조합이 가능하도록 하기 위해 배치
                # e 값을 비교해서 순서배열
                if e < t_ch[-1][0]:
                    continue

            visit[cx][cy] = 1 # 특정 치킨집 방문 처리
            # t_ch에는 치킨집을 m개 만큼 넣고 비교
            t_ch.append((e,(cx,cy)))
            select_chicken(cnt+1)
            visit[cx][cy] = 0 # 특정 치킨집 방문 철회
            t_ch.pop()

n,m = map(int, input().split())
l = [list(map(int,input().split())) for _ in range(n)]
house = []
chick = []
visit = [[0]*(n) for _ in range(n)]
t_ch = []
res = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            house.append((i,j))
        elif l[i][j] == 2:
            chick.append((i,j))

select_chicken(0)
print(res)
print(min(res))