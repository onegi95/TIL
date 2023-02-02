import sys
sys.stdin = open('input.txt')

T = int(input())

num_list = list(map(int, input().split()))

dp = [0] * T

for i in range(T):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[j]>dp[i]:
            dp[i] = dp[j]
    dp[i] +=1

print(max(dp))