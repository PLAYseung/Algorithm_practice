import sys

def main():
    n,m = map(int,input().split())

    w = list(map(int,input().split()))

    r = []
    for i in range(m): r.append(list(map(int,input().split())))
    
    relation = {}
    for item in r:
        for i in range(len(item)):
            if item[i] in relation.keys():
                relation[item[i]].append(item[i-1])
            else:
                relation[item[i]] = [item[i-1]]

    # print(w)
    # print(relation)

    cnt = 0
    for i in range(n):
        if i+1 in relation.keys():
            com = w[i]
            com_cnt = 0
            for j in range(len(relation[i+1])):
                if com > w[relation[i+1][j]-1]:
                    # print(f'키값 : {i+1} 벨류값 : {w[relation[i+1][j]-1]}, 키값이 있고 키값이 더 큼')
                    com_cnt+=1
            if com_cnt == len(relation[i+1]):
                cnt +=1
        else:
            # print(f'{i} 번째 키값 없음')
            cnt+=1

    print(cnt)

if __name__=='__main__':
    main()