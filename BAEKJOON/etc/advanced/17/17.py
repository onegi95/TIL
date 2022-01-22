import sys
sys.stdin = open('input.txt')

# 확산 관련 함수 만들기
#
# T = int(input())
#
# for tc in range(1, T+1):
N, K = map(int, input().split()) # 맵의 넓이, 바이러스 개수
virus_map = [[]for _ in range(K+1)]
lab_map = []
# 맵 생성
for i in range(N):
    lab_map.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if lab_map[i][j] !=0:
            virus_map[lab_map[i][j]].append([i,j])
S, Y, X = map(int, input().split())
dxx = [0, 0, 1, -1]
dyy = [1, -1, 0, 0]
time = 0
while time < S and lab_map[Y - 1][X - 1] == 0:
    for i in range(1,K+1): # 바이러스 종류
        temp_stack = []
        while virus_map[i]:
            temp = virus_map[i].pop(0)
            temp_y = temp[0]
            temp_x = temp[1]
            for t in range(4):

                dy = temp_y + dyy[t]
                dx = temp_x + dxx[t]
                if 0 <= dx < N and 0 <= dy < N and lab_map[dy][dx] == 0:
                    lab_map[dy][dx] = i
                    temp_stack.append([dy,dx])
        virus_map[i] = temp_stack
    time += 1
print(lab_map[Y-1][X-1])



