import sys
sys.stdin = open('input.txt')


# 감염 확산하는 파트
def dfs(danger_point_x, danger_point_y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    lab[danger_point_y][danger_point_x] = 2
    for i in range(4):
        flue_x = danger_point_x + dx[i]
        flue_y = danger_point_y + dy[i]
        if 0 <= flue_x < M and 0 <= flue_y < N and lab[flue_y][flue_x] == 0:
            dfs(flue_x, flue_y)


T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    all_lab = []
    empty_space = []
    danger_space = []
    for j in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        for i in range(len(temp)):
            if temp[i] == 0: # 안전지대는?
                empty_space.append([j,i])
            elif temp[i] == 2: # 바이러스 지대는?
                danger_space.append([j,i])
        all_lab.append(temp)
    maximun = 0

    # 빈자리에 격벽 세우는 파트
    for i in range(len(empty_space)-2):
        for j in range(i+1,len(empty_space)-1):
            for k in range(j+1,len(empty_space)):
                lab = [([0] * M) for _ in range(N)]
                # temp lab 생성
                for y in range(N):
                    for x in range(M):
                        lab[y][x] = all_lab[y][x]

                lab[empty_space[i][0]][empty_space[i][1]] = 1
                lab[empty_space[j][0]][empty_space[j][1]] = 1
                lab[empty_space[k][0]][empty_space[k][1]] = 1
                # 감염 확산하는 파트
                for q in range(len(danger_space)):
                    dfs(danger_space[q][1], danger_space[q][0])

                count = 0
                for y in range(N):
                    for x in range(M):
                        if lab[y][x] == 0:
                            count += 1
                if count > maximun:
                    maximun = count

    print(maximun)