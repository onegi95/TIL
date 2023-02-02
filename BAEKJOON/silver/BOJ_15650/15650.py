import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    pb_list = [i+1 for i in range(n)]
    anw_list  = []

    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(pb_list[j])
        if len(temp) == m:
            anw_list.append(temp)
    anw_list.sort()
    for an in anw_list:
        for real in an:
            print(real,end=' ')
        print()
