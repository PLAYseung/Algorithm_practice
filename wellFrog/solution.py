import sys

def main():
    n,m = map(int,input().split())
    w = list(map(int,input().split()))
    isBest = [True]*n
    cnt = 0

    for _ in range(m):
        A,B = map(int,input().split())

        if w[A-1] > w[B-1]:
            isBest[B-1] = False
        elif w[A-1] < w[B-1]:
            isBest[A-1] = False
        else:
            isBest[A-1] = False
            isBest[B-1] = False
    
    for member in isBest:
        if member==True:
            cnt+=1
    
    print(cnt)


if __name__=='__main__':
    main()