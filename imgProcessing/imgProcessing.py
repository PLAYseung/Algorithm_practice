import sys
from collections import deque
#  
def compare(i,j):

    pass


def main():
    h,w = map(int,input().split())
    img = []
    for _ in range(h): img.append(list(map(int,input().split())))
    n = int(input())

    for _ in range(n):
        que = []
        i,j,c = map(int,input().split())
        i = i-1
        j = j-1
        que.append([i,j])
        while que:
            if img[i][j] == img[i-1][j] :
                if [i-1,j] not in que:
                    que.append([i-1,j])
            if img[i][j] == img[i+1][j]:
                if [i-1,j] not in que:
                    que.append([i+1,j])
            if img[i][j] == img[i][j-1]:
                if [i-1,j] not in que:
                    que.append([i,j-1])
            if img[i][j] == img[i][j+1]:
                if [i-1,j] not in que:
                    que.append([i,j+1])
            
            i,j = que.pop()
            img[i][j] = c

    print(img)

    pass

if __name__=='__main__':
    main()