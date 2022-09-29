import sys
from collections import deque


N, M = map(int, input().split())
map_list = []
for _ in range(N):
    map_list.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a,b,c = queue.popleft()

        if a== (N-1) and b == (M-1):
            return visited[a][b][c]
        for i in range(4):
            mvx = a + dx[i]
            mvy = b + dy[i]
            if  0> mvx or mvx>=N or 0> mvy or mvy>=M :
                continue
                # 가려는 곳이 벽이고, 아직 기회를 안 썼을때
            if map_list[mvx][mvy] == 1 and c ==0:
                visited[mvx][mvy][1] = visited[a][b][0] + 1
                queue.append((mvx,mvy,1))
            # 가려는 곳이 벽이 아닐경우
            elif map_list[mvx][mvy] == 0 and visited[mvx][mvy][c] == 0:
                visited[mvx][mvy][c] = visited[a][b][c] + 1
                queue.append((mvx, mvy, c))
    return -1


print(bfs(0,0,0))