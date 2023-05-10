def solution(people, limit):
    '''
    테스트케이스만 통과하는 코드 조정 필요
    '''
    ans = 0
    st = 0
    weight = 0

    people.sort()

    for i in range(len(people)-1,st-1,-1):
        for j in range(st,len(people)):
            if people[i]==people[j]:
                return ans+1
            weight = limit - people[i]
            if weight < people[j]:
                break
            else:
                st += 1
                break
        ans +=1