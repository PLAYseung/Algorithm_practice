import sys

message = input()
key = input()

key_table = [[0 for i in range(5)] for i in range(5)]
used_c = {}

for i in range(len(key)):
    if key[i] not in used_c:
        key_table[len(used_c)//5][len(used_c)%5] = key[i]
        used_c[key[i]] = len(used_c)

for k in range(26):
    c = chr(ord('A') + k)
    if c == 'J': continue
    if c not in used_c:
        key_table[len(used_c)//5][len(used_c)%5] = c
        used_c[c] = len(used_c)

split_message = []
i = 0
message_m = ''

while i<len(message):
    if i == len(message) -1:
        split_message.append(f'{message[i]}X')
        break
    elif message[i] != message[i+1]:
        split_message.append(message[i:i+2])
        i += 2
    elif message[i] == message [i+1]:
        if message[i] != 'X':
            split_message.append(f'{message[i]}X')
            i += 1
        else:
            split_message.append(f'{message[i]}Q')
            i += 1
    
for i in split_message:
    x1, x2 = i[0], i[1]
    x1_loc = used_c[x1]
    x2_loc = used_c[x2]
    if x1_loc//5 == x2_loc//5:
        m1 = (x1_loc+1)%5
        m2 = (x2_loc+1)%5
        x1_m = key_table[x1_loc//5][m1]
        x2_m = key_table[x2_loc//5][m2]
    elif x1_loc%5 == x2_loc%5:
        m1 = (x1_loc//5+1) if (x1_loc//5)<4 else 0
        m2 = (x2_loc//5+1) if (x2_loc//5)<4 else 0
        x1_m = key_table[m1][x1_loc%5]
        x2_m = key_table[m2][x2_loc%5]
    else:
        x1_m = key_table[x1_loc//5][x2_loc%5]
        x2_m = key_table[x2_loc//5][x1_loc%5]
    message_m = message_m + x1_m + x2_m

print(message_m)