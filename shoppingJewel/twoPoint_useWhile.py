from collections import defaultdict


def solution(gems):
    answer = [0, 0]
    candidates = []
    start, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    
    while True:
        kind = len(gems_dict)
        # 주어진 보석이 없을 경우
        if start == gems_len:
            break
        # 보석의 갯수 만큼 키:벨류 가 생성됬을 때
        # 보석의 처음 부터 유니크 값보다 작아질 때 까지 반복
        if kind == gem_kind:
            # 튜플 형태로 서치 형태를 저장
            candidates.append((start, end))
            # gems_dict가 가지고 있는 값들을 0으로 내리기 위함
            gems_dict[gems[start]] -= 1

            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        # 끝까지 돌아도 유니크 값이 나오지 않음
        if end == gems_len:
            break
        # 딕셔너리의 갯수가 유니크 값(갯수) 보다 작을 때
        if kind != gem_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue

    length = float('inf')
    for s, e in candidates:
        if length > e-s:
            length = e-s
            answer[0] = s + 1
            answer[1] = e
    return answer


if __name__=='__main__':
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))