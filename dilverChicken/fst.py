# sol1. 어느 곳을 기준으로? 집 
# 집을 기준으로 방문한 위치에 있는 치킨집에 거리를 부여 
# -> 치킨집에 쌓인 수를 기준으로 정렬 
# -> 가장 작은 M개 많큼 더하기
# 문제해결 x


n,m = map(int, input().split())
chicken = [[]*n]*n
check = [[]*n]*n
town = []*n
for i in range(n):
    town.append(input().split())

# 1. 집을 기준(r,c)으로 뻗어 나가면서 2를 만날 때까지 반복
# 2. 2를 만났다면 돌아(재귀)가면서 +1
# 3. 집으로 돌아왔을때 값을 치킨집에 더해줌
# 반환되는 값 : 치킨집 좌표(r,c), 거리
def house(town,r,c,check):
    check[r][c] = 1
    nr,nc = 0,0
    store = [0,0,0]
    while 1:
        nc+=1
        if n == nc:
            nc = 0
            nr += 1
        if nr == n:
            return store
        if town[r][c] == 2:
            if abs(r-nr)+abs(c-nc) > store[2]:
                store = [nr,nc,abs(r-nr)+abs(c-nc)]

for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            print(f'{i} / {j}')
            r,c,dist = house(town, i, j, check).split()
            chicken[r][c] += dist

storeList = []
for i in range(n):
    for j in range(n):
        print(f'{i} / {j}')
        if chicken[i][j]:
            storeList.append(chicken[i][j])

storeList.sort(reverse=True)

result = 0
for i in range(m-1):
    result+=storeList[i]

print(result)