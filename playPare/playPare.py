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
    for i in range(0,len(massege),2):
        cy_key.append(massege[i:i+2])
    

    cy_key_idx = list()
    for idx,item in enumerate(cy_key):
        each_list = list()
        for char in item:
            for i in range(5):
                for j in range(5):
                    if char == key_map[i][j]:
                        each_list.append([i,j])
        cy_key_idx.append(each_list)


    for idx,char_set in enumerate(cy_key_idx):
        if char_set[0][0] == char_set[1][0]:
            if cy_key_idx[idx][0][1] < 4:
                cy_key_idx[idx][0][1] += 1
            else:
                cy_key_idx[idx][0][1] = 0

            if cy_key_idx[idx][1][1] < 4:
                cy_key_idx[idx][1][1] += 1
            else:
                cy_key_idx[idx][1][1] = 0

        elif char_set[0][1] == char_set[1][1]:
            if cy_key_idx[idx][0][0] < 4:
                cy_key_idx[idx][0][0] += 1
            else:
                cy_key_idx[idx][0][0] = 0

            if cy_key_idx[idx][1][0] < 4:
                cy_key_idx[idx][1][0] += 1
            else:
                cy_key_idx[idx][1][0] = 0

        else:
            cy_key_idx[idx][0][1],cy_key_idx[idx][1][1] = cy_key_idx[idx][1][1],cy_key_idx[idx][0][1]
        


    answer = ''
    for char_set in cy_key_idx:
        for char in char_set:
            pass
            answer += key_map[char[0]][char[1]]

    print(answer)

if __name__=='__main__':
    main()
