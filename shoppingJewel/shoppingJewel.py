def solution(gems):
    answer = []
    unq_gem = len(list(set(gems)))
    copy_gems = []
    for idx in range(len(gems)):
        if unq_gem != len(list(set(gems[idx:]))):
            copy_gems = gems[idx-1:]
            answer.append(idx-1)
            break
    for idx in range(len(copy_gems)):
        if unq_gem != len(list(set(copy_gems[:len(copy_gems)-idx]))):
            answer.append(len(gems) - idx+1)
            return(answer)


if __name__=='__main__':
    print(solution(	["AA", "AB", "AC", "AA", "AC"]))