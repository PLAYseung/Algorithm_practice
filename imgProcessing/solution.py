import sys

def main():
    sys.setrecursionlimit(10**5)
    h,w = map(int,sys.stdin.readline().split())
    # 탐색 지점의 최외각 지점을 표현해주기 위해서 입력 이미지 보다 1크게 만든다 (여백)
    img = [[0]*(w+2)]
    for _ in range(h): img.append([0] + list(map(int,sys.stdin.readline().split()))+ [0])
    img.append([0]*(w+2))

    n = int(sys.stdin.readline())

    # dfs 재귀 함수 작성 법
    # 탐색할 대상에 대해서 조건을 지정 해준다
    def color(x,y,c):
        oldc = img[x][y]
        img[x][y] = c
        if img[x-1][y] == oldc:
            color(x-1,y,c)
        if img[x+1][y] == oldc:
            color(x+1,y,c)
        if img[x][y-1] == oldc:
            color(x,y-1,c)
        if img[x][y+1] == oldc:
            color(x,y+1,c)
        return
        
    for k in range(n):
        x,y,c = map(int,sys.stdin.readline().split())
        if img[x][y] != c:
            color(x,y,c)


    for i in range(1,h+1):
        for j in range(1,w+1):
            print(img[i][j],end=' ')
        print()


if __name__=='__main__':
    main()