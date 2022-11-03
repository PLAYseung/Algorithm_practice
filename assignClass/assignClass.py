import sys
import heapq

def main():
    n = int(input())

    cls = []

    for _ in range(n): 
        s,f = map(int,input().split())
        
        # f를 기준으로 (f,s)가 리스트안에 들어감
        heapq.heappush(cls,(f,s))

    v = 0

    cnt = 0

    print(cls)
    while cls:
        # 가장 작은 f를 기준으로 원소를 획득
        f,s = heapq.heappop(cls)

        # 시작 시간이 종료시간 보다 크거나 같으면 카운트
        # 다음 기준값은 카운트한 종료 시간으로 초기화
        if s>=v:
            cnt += 1
            v = f

    print(cnt)

if __name__=='__main__':
    main()