n, m = map(int, input().split())
answer = float('inf')

house, chicken = [], []

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))

def dfs(idx,cnt):
    global answer, chicken, m

    if idx > len(chicken):
        return
    if cnt == m:
        total_distance = 0
        for r1,c1 in house:
            distance = float('inf')
            for i, pos in enumerate(chicken):
                if checked[i]:
                    r2,c2 = pos
                    distance = min(distance, abs(r1-r2)+abs(c1-c2))
            total_distance += distance
        answer = min(answer, total_distance)

    checked[idx] = True
    dfs(idx+1, cnt+1)
    checked[idx] = False

checked = [False] *(len(chicken)+1)
dfs(0, 0)

print(answer)