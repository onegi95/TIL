import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
anw = 1
if n == m :
    print(1)
else:
    high = n-m+1
    # n~higt 까지 곱
    top = 1
    bottom = 1
    for i in range(m):
        top = top*(n-i)
    for j in range(m):
        bottom = bottom*(1+j)
    print(int(top//bottom))