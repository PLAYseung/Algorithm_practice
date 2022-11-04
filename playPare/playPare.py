import sys
import string

def main():
    sys.setrecursionlimit(10**5)
    massege = list(sys.stdin.readline())
    key = sys.stdin.readline()

    massege.remove('\n')

    use_alpha = []
    base = list(string.ascii_uppercase)
    base.remove('J')

    for st in key:
        if st in use_alpha:
            continue
        else:
            use_alpha.append(st)
            if st in base:
                base.remove(st)

    base = use_alpha + base
    base.remove('\n')

    key_map = [[],[],[],[],[]]
    alpha_num = 0
    for i in range(5):
        for j in range(5):
            key_map[i].append(base[alpha_num])
            alpha_num+=1

    idx = 0
    while True:
        if idx == len(massege)-1:
            break
        if massege[idx]==massege[idx+1]:
            if massege[idx]=='X':
                massege.insert(idx+1, 'Q')
            else:
                massege.insert(idx+1, 'X')
            pass
            idx += 1
        idx += 1
    
    if len(massege)%2!=0:
        massege.append('X')

    cy_key = []
    
    pass

if __name__=='__main__':
    main()