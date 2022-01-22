import sys
T = int(input())
for tc in range(1,T+1):
    N, M, K, X = map(int, sys.stdin.readline().split()) # 도시개수, 도로개수, 거리정보, 출발도시 번호
    num_map = [[] for _ in range(N+1)]
    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        num_map[start].append(end)

    # 최초방문, 방문거리 K
    visited = [0]*(N+1)
    start_point = X
    new_start = [X]
    road = 0
    visited[X] = 1
    while True:
        road += 1
        temp_start = []
        for j in range(len(new_start)):
            start_point = new_start.pop(0)
            if visited[start_point] > 1:
                break
            for i in num_map[start_point]:
                if visited[i] == 0:
                    temp_start.append(i)
                    visited[i] +=1
        new_start = temp_start
        if road == K:
            break
    if new_start:
        new_start.sort()
        for i in new_start:
            print(i)

    else:
        print(-1)