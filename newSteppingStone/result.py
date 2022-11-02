import sys

def main():
    num = int(input())
    rocks = list(map(int,input().split()))

    # 해당 번째의 돌 보다 작은 높이의 돌들의 갯수 +1
    result = [1] *num

    for i in range(1,num):
        # 밟을 수 있는 돌의 갯수 비교용
        result_max = 0

        for j in range(i):
            
            #다음 밟을 돌의 높이와 그전에 있는 모든 돌의 높이 비교
            if rocks[i] > rocks[j]:
                if result_max < result[j]:
                    result_max = result[j]
        result[i] = result_max + 1

    print(max(result))
    pass

if __name__=='__main__':
    main()