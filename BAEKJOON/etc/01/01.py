import sys
sys.stdin = open('input.txt')

N = int(input())

numbers = list(map(int, input().split()))

num_list = sorted(numbers)
new_list = []
for i in range(1,len(num_list)+1):
    new_list.append(num_list[-i])

# 파티 묶어주기
count = 0
while len(new_list) >0:
    # 탈출 조건
    if new_list[0] > len(new_list):
        break

    # 묶어서 보내기
    k = new_list[0]
    del[new_list[:k]]
    count+=1

print('최대 파티 수는? {}'.format(count))
# 반례가 있을까?