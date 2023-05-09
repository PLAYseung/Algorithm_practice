def solution(s):
    '''
    앞뒤를 비교해주기 위한 임시 리스트를 사용
    '''
    stack = []
    s = list(s)

    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    if not stack: return 1
    return 0