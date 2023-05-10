def solution(n, words):
    '''
    앞에서 나온 단어를 저장하기 위한 리스트로 나왔는지 체크
    인덱스값을 기준으로 결과 반환
    [ 나머지+1 , 몫+1 ]
    '''
    word = []
    w_len = len(words)
    for i in range(len(words)):
        if not word:
            word.append(words[i])
        else:
            if not (words[i][0] == word[i-1][-1]) or (words[i] in word):
                return [(i%n)+1,(i//n)+1]
            else:
                word.append(words[i])
    return [0,0]