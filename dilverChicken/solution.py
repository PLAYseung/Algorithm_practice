n, m = map(int, input().split())
# 비교를 통해 작은 값을 저장해야 하기 때문에 가장 큰 값으로 설정
answer = float('inf') # 양의 무한대; 음의 무한대: -inf

house, chicken = [], []

for i in range(n):
    # 빈칸은 알필요 없기 때문에 집과 치킨집의 좌표만 각각 저장
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))

# 현재 치킨집의 인덱스 : idx, 확인된 치킨집의 수 : cnt
def dfs(idx,cnt):
    global answer, chicken, m

    # 마지막에 있는 치킨집 인덱스까지 확인후 종료
    if idx > len(chicken):
        return
    # 마지막 치킨집 인덱스에 도달
    # m의 최대 값은 치킨집의 수랑 같기 때문
    if cnt == m:
        total_distance = 0
        # house의 안에 리스트로 존재 하기때문에 r1,c1으로 변수를 받음
        for r1,c1 in house:
            # 가장 작은 값을 받을 것이기 때문에 무한대
            distance = float('inf')
            for i, pos in enumerate(chicken):
                # checked에 있는 치킨집에 대해서만 계산
                if checked[i]:
                    r2,c2 = pos
                    # checked에 있는 치킨집 중에 가장 거리가 짧은 값을 distance에 저장
                    distance = min(distance, abs(r1-r2)+abs(c1-c2))
            # 가장 작은 값을 누적
            total_distance += distance
        # 누적시킨 값과 이전에 동작한 값을 비교후 작은값을 저장
        answer = min(answer, total_distance)

    # 현재 치킨집을 기준으로 m개까지 확인 하기 위해사용
    checked[idx] = True
    # 현재 치킨집 인덱스부터 m개까지 재귀
    dfs(idx+1, cnt+1)
    # 현재 위치를 초기화
    checked[idx] = False

# checked[idx] = True가 마지막 치킨집에서 한번더 실해되기 때문에 checked의 인덱스는 치킨집보다 1큰 크기를 보유
checked = [False] *(len(chicken)+1)
dfs(0, 0)

print(answer)