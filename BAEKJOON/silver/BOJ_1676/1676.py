import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    temp = 1
    for i in range(1,N+1):
        temp = temp*i
    temp = str(temp)
    anw = 0
    for k in range(1, len(temp)):
        if temp[-k] != '0':
            break
        else:
            anw +=1

    print(anw)