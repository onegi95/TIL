import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())


num_list = list(map(int, input().split()))

num_list.sort()

for i in range(1,len(num_list)):
    num_list[i] = num_list[i-1] + num_list[i]
print(sum(num_list))


