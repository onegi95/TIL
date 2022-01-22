n, m = map(int, input().split(' ')) # 
num_list = [[]]*n
for i in range(n):
    num_list[i] = list(map(int, input().split(' ')))

check_list = []
for i in num_list:
    check_list.append(min(i))

print(max(check_list))