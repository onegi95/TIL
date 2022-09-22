import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')


def bellman_ford(start):
    distance[start] = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
           for vec ,wei in road[j]:
               if distance[vec] > wei + distance[j]:
                   distance[vec] = wei + distance[j]
                   if i == N:
                        return True
    return False
T = int(input())

for tc in range(T):
    # 지점의 갯수, 도로의 갯수, 웜홀의 갯수
    N, M, W = map(int, input().split())
    road = [[] for _ in range(N+1)]
    distance = [9999999999999999 for _ in range(N+1)]

    for i in range(M):
        a, b, c = map(int, input().split())
        road[a].append([b,c])
        road[b].append([a, c])

    for i in range(W):
        a, b, c = map(int, input().split())
        road[a].append([b,-c])

    bp = bellman_ford(1)
    if not bp:
        print("NO")
    else:
        print("YES")