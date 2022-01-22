import sys
sys.stdin = open('input.txt')
def dfs(y,x):
    ice_map[y][x] = 1
    go_way_x = [1,-1,0,0]
    go_way_y = [0, 0, 1, -1]
    for i in range(4):
        dx = x + go_way_x[i]
        dy = y + go_way_y[i]
        if 0<= dx <N and 0 <= dy <T and ice_map[dy][dx] == 0:
            dfs(dy,dx)

T,N = map(int,input().split())
ice_map = []
for _ in range(T):
    ice_map.append(list(map(int,input())))
ice_count = 0
for i in range(T):
    for j in range(N):
        if ice_map[i][j] == 0:
            dfs(i,j)
            ice_count += 1
print(ice_count)
