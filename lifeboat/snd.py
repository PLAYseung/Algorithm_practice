def solution(people,limit):
    '''
    앞에서 부터 뒤로 뒤에서 부터 앞으로 한칸씩 이동 하는 형식으로 값을 비교
    모두 혼자 이용하는 경우 lst와 fst가 0으로 일치하기 때문에 +1
    '''
    fst = 0
    lst = len(people)-1
    ans = 0

    people.sort()

    while fst<lst:
        if people[lst] + people[fst] > limit:
            lst -= 1
        else:
            lst-=1
            fst+=1
        ans +=1
        
    if lst == fst: ans +=1
    return ans


# 50 50 70 80