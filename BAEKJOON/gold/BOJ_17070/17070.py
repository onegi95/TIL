import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    #  초기셋팅
    N = int(input())

    pipe_map = []

    for _ in range(N):
        temp = list(map(int, input().split()))
        pipe_map.append(temp)

    dp_map = [[0 for _ in range(N)]for _ in range(N)]
