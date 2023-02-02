import sys
sys.stdin = open('input.txt')

T = int(input())

def requl(a,b):
    global m,n
    if a > m:
        for k in anw_list:
            print(k,end=' ')
        print()
        return
    for i in range(b,n+1):
        anw_list.append(i)
        requl(a+1,i)
        anw_list.pop()

for tc in range(T):
    n, m = map(int, input().split())

    anw_list  = []
    requl(1,1)