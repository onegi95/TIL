import sys
sys.stdin = open('input.txt')
import heapq

INF = int(1e9)
V, E = map(int ,sys.stdin.readline().split()) # V : 정점의 수, E : 간선의 수

start_point = int(input())

# 정점과 연결된 간선
line = [[] for _ in range(V+1)]

for i in range(E):
    u,v,w = map(int, sys.stdin.readline().split()) # u에서 v 로 가는 가중치 w
    line[u].append([v,w])

# 다익스트라

def dijkstra(start):
    q = []
    distance = [INF] * (V + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in line[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance



go = dijkstra(start_point)

for i in range(1,len(go)):
    if go[i] != INF:
        print(go[i])
    else:
        print('INF')
