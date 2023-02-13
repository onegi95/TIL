import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n,m = map(int, input().split())
road_map = []
for _ in range(n):
    temp = list(map(int, input().split()))
    road_map.append(temp)
sum_map = [[0]*(n+1) for _ in range(n+1)]
# print(sum_map)
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_map[i][j] = sum_map[i-1][j] + sum_map[i][j-1] - sum_map[i-1][j-1] + road_map[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(sum_map[x2][y2] - sum_map[x1 -1][y2] - sum_map[x2][y1-1] + sum_map[x1-1][y1-1])
