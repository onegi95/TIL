import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

linear_list = [0] * (N+1)
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

anchor_num = num_list[0]
high_num = num_list[0]
num_list.pop(0)
err_point = 0
anw_list = []
for i in range(high_num):
    anw_list.append('+')
anw_list.append('-')
while num_list:
    temp = num_list.pop(0)
    high_num = max(high_num, temp)
    linear_list[anchor_num] = 1
    if temp < anchor_num :
        # 안되는 경우
        for i in range(anchor_num-temp):
            if linear_list[anchor_num-i] != 1:
                err_point  = 1
                print('NO')
                quit()


    # + 를 더하는 경우
    else:
        for i in range(high_num - anchor_num):
            if linear_list[anchor_num + i + 1] == 1:
                pass
            else:
                anw_list.append('+')
    anw_list.append('-')
    anchor_num = temp
if err_point == 1:
    print('NO')
else:
    for i in anw_list:
        print(i)
