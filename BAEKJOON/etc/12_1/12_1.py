import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = list(map(int,input()))
    half = int(len(N)/2)
    a = sum(N[0:half])
    b = sum(N[half:])
    if a == b:
        print('LUCKY')
    else:
        print('READY')  
