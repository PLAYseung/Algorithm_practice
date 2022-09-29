def solution(gems):
    st, ed = 0, 0
    finsh_option = len(list(set(gems)))

    for idx in range(len(gems)+1):
        if finsh_option == len(list(set(gems[:idx]))):
            ed = idx
            break
    for idx in range(len(gems)+1):
        if finsh_option != len(list(set(gems[idx:ed]))):
            st = idx
            return [st,ed]
    pass

if __name__=='__main__':
    print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"] ))