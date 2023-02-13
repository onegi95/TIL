import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    temp = list(map(str, input()))
    char_temp = ''
    cal_list =   []
    mi_list = []
    triger = 0
    last_char = 0
    for i in temp:
        if i == '-' and triger == 0:
            cal_list.append(int(char_temp))
            char_temp = ''
            triger = 1
            last_char = 1
        elif i == '-' and triger == 1:
            mi_list.append(int(char_temp))
            char_temp = ''
            triger = 1
            last_char = 1
        elif i == '+' and triger == 0:
            cal_list.append(int(char_temp))
            char_temp = ''
            last_char = 0
        elif i == '+' and triger == 1:
            mi_list.append(int(char_temp))
            char_temp = ''
            last_char = 0
        else:
            char_temp = char_temp + i

    if triger == 0 and last_char == 0:
        cal_list.append(int(char_temp))
    elif triger == 0 and last_char == 1:
        mi_list.append(int(char_temp))
    elif triger == 1 and last_char == 0:
        mi_list.append(int(char_temp))
    else:
        mi_list.append(int(char_temp))
    print(sum(cal_list) - sum(mi_list))

