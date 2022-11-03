import sys

def main():
    K,P,N = map(int,input().split())

    # (P의 N*10 제곱을 1000000007로 나눈 나머지 * K)를 1000000007로 나눈 나머지
    print((K*pow(P,N*10,1000000007))%1000000007)
    pass

if __name__=='__main__':
    main()