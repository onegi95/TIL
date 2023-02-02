import sys
sys.stdin = open('input.txt')


n,m = map(int, input().split())
road_map = []
for _ in range(n):
    temp = list(map(int, input().split()))
    road_map.append(temp)



for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    temp = 0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            temp += road_map[i][j]
    print(temp)
