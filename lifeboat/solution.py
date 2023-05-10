import fst,snd

people = [[70, 50, 80, 50],[70, 80, 50]]
limit = [100,100]

for i in range(len(limit)):
    print(snd.solution(people[i],limit[i]))