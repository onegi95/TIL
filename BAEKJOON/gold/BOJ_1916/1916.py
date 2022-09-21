import sys
from heapq import heappush,  heappop
sys.stdin = open('input.txt')

# bp

def dijkstra(start):
    heap = []
    heappush(heap, (0,start) )
    distance[start] = 0

    while heap:
        dist, now = heappop(heap)

        if distance[now] < dist:
            continue

        for i in bus_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))




N =int(input())
M = int(input())
bus_list  = list([] for _ in range(N+1))
distance = [9999999999999999] * (N+1)

for i in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    bus_list[temp[0]].append([temp[1],temp[2]])


start_point, end_point = map(int, input().split())

dijkstra(start_point)
print(distance[end_point])