import sys
sys.stdin = open('input.txt')

T = int(input())

def fivonachi(n):
    global num_zero, num_one
    if n == 0:
        temp = [1,0]
        return temp
    elif n == 1:
        temp = [0,1]
        return temp
    else:
        if  dp[n][2] == 0:
            a = fivonachi(n-1)
            b = fivonachi(n-2)
            dp[n][0] += a[0] + b[0]
            dp[n][1] += a[1] + b[1]
            dp[n][2] = 1
            return dp[n]
        else:
            return dp[n]



for tc in range(T):
    num_zero = 0
    num_one = 0
    k = int(input())
    dp = [[0,0,0] for _ in range(k+1) ]
    fivonachi(k)
    if k == 0:
        print(1, 0)
    elif k ==1:
        print(0, 1)
    else:
        print(dp[-1][0] , dp[-1][1])

