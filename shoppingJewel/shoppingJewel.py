def solution(gems):
    answer = []
    unq_gem = list(set(gems))
    print(unq_gem)

    return answer

if __name__=='__main__':
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))