import sys

def main():
    N,K = map(int,input().split())

    S = list(map(int,input().split()))

    for idx in range(K):
        st,en = map(int,input().split())
        num = sum(S[st-1:en])/len(S[st-1:en])

        print(f'{num:.2f}')
    pass

if __name__=='__main__':
    main()