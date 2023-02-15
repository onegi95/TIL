import sys
import time
sys.stdin = open('input.txt')

input = sys.stdin.readline

def diffusion(x,y,a):
    """
    오염물질이 있는 부분의 좌표, 오염물질의 양을 받아 어떤 위치로 분산이 일어나는지 알아보는 함수
    input : x,y,a = (퍼지는 대상이 되는 부분의 좌표와 현재 보유하고 있는 오염물질의 양
    output(LIST) : 이 위치에서 일어나는 분산에 대한 변경값의 모음
    """
    move_x = [0,0,-1,1]
    move_y = [-1,1,0,0]
    diffusion_amount = a//5
    go_mount = 0
    go_position = []
    for i in range(4):
        moving_x = x + move_x[i]
        moving_y = y + move_y[i]
        if 0<= moving_x and moving_x <  R and 0 <= moving_y and moving_y < C:
            if air_map[moving_x][moving_y] != -1:
                go_mount += 1
                go_position.append([moving_x,moving_y,diffusion_amount])
    go_position.append([x,y,-(diffusion_amount*go_mount)])
    return go_position

def air_check():
    air_checks = []
    for i in range(R):
        for j in range(C):
            if air_map[i][j] >4:
                air_checks.append([i, j, air_map[i][j]])
    return air_checks


def air_condition(conditiona_point):
    condition_1 = conditiona_point
    condition_2 = conditiona_point+1
    temp = []
    for j in range(1, condition_1 + 1):
        temp.append([j, 0, air_map[j-1][0]]) #1왼
    for i in range(1, C):
        temp.append([0, i - 1, air_map[0][i]])  # 1가로위
    for j in range(1,condition_1+1):
        temp.append([j-1,C-1,air_map[j][C-1]]) #1오른
    for i in range(1,C-1):
        temp.append([condition_1,i+1,air_map[condition_1][i]]) # 1가로밑
    for u in range(condition_2+1,R-1):
        temp.append([u, 0, air_map[u+1][0]])  # 2왼
    for i in range(1, C):
        temp.append([R-1, i - 1, air_map[R-1][i]])  # 2가로밑
    for k in range(condition_2+1,R):
        temp.append([k, C - 1, air_map[k-1][C - 1]])  # 2오른
    for i in range(1, C - 1):
        temp.append([condition_2, i + 1, air_map[condition_2][i]])  # 2가로위






    return temp


T = int(input())

for tc in range(T):
    start = time.time()
    R, C, Ts = map(int, input().split())
    air_map = []
    for _ in range(R):
        air_map.append(list(map(int, input().split())))

    #     공기 청정기 위치 확인
    no_t = 0
    while True:
        if air_map[no_t][0] == -1:
            conditiona = no_t
            break
        no_t+=1


    #   공기 청정기로 인한 순환 확인

    #  확산도 확인을 해야 되는데.... 그렇다고 bf로 모두 체크하자니 일이 너무 많다
    for _ in range(Ts):
        temp = air_check()
        go = []
        for x,y,a in temp:
            go = go +  diffusion(x,y,a)
        for x1,y1,a1 in go:
            air_map[x1][y1] += a1
        temp2 = air_condition(conditiona)
        for x,y,a in temp2:
            air_map[x][y] = a
        air_map[conditiona][0] = -1
        air_map[conditiona+1][0] = -1
        air_map[conditiona][1] , air_map[conditiona+1][1] = 0,0

    anw = 0


    for i in range(R):
        for j in range(C):
            anw += air_map[i][j]
    print(anw+2)
    #  그럼 dp 맵을 하나 만들어서, 좌표 + 먼지 이동량 으로 계산하는 건 어떨까? =>

    # 이동량을 계산한 다음 => 다시 적용시켜 주는 것


