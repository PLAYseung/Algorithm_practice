def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        cross = (left + right) // 2
        cnt = 0
        for t in stones:
            if t - cross <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = cross - 1
        else:
            left = cross + 1
        
    return left

if __name__=='__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3))
