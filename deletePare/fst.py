def solution(s):    
    '''
    테스트 케이스 3개 통과
    시간 초과
    '''
    s_size = len(s)
    s = list(s)
    
    while True:
        num = 0
        for idx in range(len(s)):
            try:
                if s[idx] == s[idx+1]:
                    s.pop(idx)
                    s.pop(idx)
            except:
                num = idx
        if len(s)==0 or len(s)==s_size:
            if len(s) < 1:
                return 1
            return 0