import sys

sys.stdin = open('input.txt')

N,M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
anw_list = []
real_list = []
used_numbers = [0 for _ in range(N+1)]

def dfs(N):
    if N-1 == M :
        print(*anw_list)
        return
    check = 0
    for an in range(len(numbers)):
        if used_numbers[an] == 0 and check != numbers[an]:
            used_numbers[an] = 1
            check = numbers[an]
            anw_list.append(numbers[an])
            dfs(N+1)
            used_numbers[an] = 0
            anw_list.pop()


dfs(1)

