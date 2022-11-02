import sys

def main():
    num = int(input())

    num = list(map(int,input().split()))

    fs_cnt = 0
    sc_cnt = 0
    com_num = 0

    for j in range(len(num)):
        for idx in range(j,len(num)):
            if num[idx] > com_num:
                com_num = num[idx]
                sc_cnt+=1
        if sc_cnt > fs_cnt:
                fs_cnt = sc_cnt

    print(fs_cnt)
    pass

if __name__=='__main__':
    main()