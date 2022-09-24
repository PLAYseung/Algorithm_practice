def solution(stones, k):
    cross = 0
    while True:
        seqZero = 0
        for idx,stone in enumerate(stones):
            if stone:
                stones[idx] -= 1
                seqZero = 0
            else:
                seqZero += 1
                if seqZero == k:
                    break
        if seqZero == k:
            break
        else :
            cross += 1
    return cross

if __name__=='__main__':
    solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	, 3)
