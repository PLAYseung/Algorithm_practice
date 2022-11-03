import sys
import bisect

def main():
    num = int(input())
    rocks = list(map(int,input().split()))

    high = [] # 앞에서부터 확인한 돌의 높이
    rev_high = [] # 뒤에서부터 확인한 돌의 높이
    cnt = [1]*num # 앞에서부터 밟은 돌의 개수
    rev_cnt = [1]*num # 뒤에서부터 밟은 돌의 개수

    # 반복문을 통해 돌의 높이 확인
    for i in range(num):

        # 앞의 돌 부터 확인

        # 확인할 돌이 없으면 현재 돌의 높이를 리스트에 추가
        if len(high) == 0:
            high.append(rocks[i])
        else:
            # 현재 돌의 높이가 리스트 마지막 돌보다 높으면
            if rocks[i]>high[-1]:
                # 리스트에 추가
                high.append(rocks[i])
            else:
                # 리스트에 마지막 돌이 더 높으면
                # 리스트에 현재 돌의 위치인덱스에 현재 돌의 높이를 초기화
                index = bisect.bisect_left(high, rocks[i])
                high[index] = rocks[i]

        # 뒤의 돌 확인

        # 제일 뒤 부터 확인 하기 때문에 n-1-i로 돌의 높이를 확인
        # 확인한 돌이 없으면 현재 돌의 높이를 리스트에 추가
        if len(rev_high) == 0:
            rev_high.append(rocks[num-1-i])
        else:
            # 현재 돌의 높이가 리스트 마지막 돌보다 높으면
            if rocks[num-1-i]>rev_high[-1]:
                # 리스트에 추가
                rev_high.append(rocks[num-1-i])
            else:
                # 리스트 마지막 돌이 더 높으면
                # 리스트에 현재 돌의 위치 인덱스에 현재 돌의 높이로 초기화
                index = bisect.bisect_left(rev_high, rocks[num-1-i])
                rev_high[index] = rocks[num-1-i]

        # 확인한 돌의 높이의 개수를 리스트에 추가
        cnt[i] = len(high)
        rev_cnt[num-1-i] = len(rev_high)

    result_target = [0]*num

    for i in range(num):
        result_target[i] = cnt[i] + rev_cnt[i]

    # 최대 값에서 두번 돌을 밟기 때문에 1을 빼줌
    print(max(result_target)-1)

if __name__=='__main__':
    main()