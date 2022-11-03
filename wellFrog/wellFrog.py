import sys

def main():
    n,m = map(int,input().split())

    w = [map(int,input().split())]

    r = []
    for i in range(m): r.append(list(map(int,input().split())))
    
    relation = {}
    for item in r:
        for i in range(len(item)):
            if item[i] in relation.keys():
                relation[item[i]].append(item[i-1])
            else:
                relation[item[i]] = [item[i-1]]

    cnt = 0
    for i in range(n):
        if i+1 in relation.keys():
            com = r[i]
            for j in range(len(relation[i+1])):
                print(r[relation[i+1][j]])
                #if com > r[relation[i+1][j]]:
                #    cnt+=1
        else:
            cnt+=1

    print(relation)
    print(cnt)

if __name__=='__main__':
    main()