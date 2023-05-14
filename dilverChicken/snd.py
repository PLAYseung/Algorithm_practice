# 맵의 크기 N x N
# 0 : 빈공간 / 1 : 집 / 2 : 치킨집
# 치킨 거리 : |r1-r2|+|c1-c2|
# m개의 치킨집만 운영
# 맵에서 치킨집 m개의 치킨집의 치킨거리가 가장 작은 경우의 값을 반환

n,m = map(int, input().split())
house = []
chicken = []

answer = 3250

for i in range(n):
    line = list(map(int,input().split()))
    for ea in range(len(line)):
        if line[ea] == 1:
            house.append((ea,i))
        elif line[ea] == 2:
            chicken.append((ea,i))


def sol(idx,cnt):
    global answer,chicken,checked,house

    # idx번째 치킨집 부터 마지막 인덱스의 치킨집이 m개 미만일 때 종료
    if idx > len(chicken):
        return
    
    # idx번째 부터 m개의 치킨집 까지의 거리를 누적으로 더함
    if cnt == m:
        totalDist = 0
        for r1, c1 in house:
            dist = 250
            for i in range(len(chicken)):
                if checked[i]:
                    r2,c2 = chicken[i]
                    dist = min(dist, abs(r1-r2)+abs(c1-c2))
            totalDist += dist
        answer = min(answer, totalDist)


    # 현재 치킨집 인덱스를 방문처리
    checked[idx] = True
    sol(idx+1,cnt+1)
    # 결과 반환 후 방문처리 초기화
    checked[idx] = False
    pass

checked = [False]*(len(chicken)+1)
sol(0,0)

print(answer)