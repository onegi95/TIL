import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
numbers = list(map(int, input().split()))
numbers.sort()
anw_list = []
check_list =  [0] * (N)

def dsf(N):
    if N-1 == M:
        print(*anw_list)
        return
    for i in range(len(numbers)):
        if check_list[i] == 0:
            anw_list.append(numbers[i])
            check_list[i] =1
            dsf(N+1)
            anw_list.pop()
            check_list[i] = 0

dsf(1)