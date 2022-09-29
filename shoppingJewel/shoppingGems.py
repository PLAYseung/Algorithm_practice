def solution(gems):
    result = []
    gems_num = len(list(set(gems)))
    copy_gems = []
    for idx in range(len(gems)-1):
        if gems_num != len(list(set(gems[:len(gems)-(idx+1)]))):
            copy_gems = gems[:len(gems)-idx]
            # print(copy_gems)
            result.insert(1,len(gems)-(idx))
            break
        elif gems_num == 1:
            result = [1,1]
            return result
    for idx in range(len(copy_gems)):
        if gems_num != len(list(set(copy_gems[idx:]))):
            # print(copy_gems[idx-1:])
            result.insert(0, idx)
            return result

if __name__=='__main__':
    print(solution(	["AA", "AB", "AC", "AA", "AC"]))