import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

row, colunm = map(int, input().split())
anw = 0
cheese_room = []
for _ in range(row):
    cheese_room.append(list(map(int, input().split())))

# blank 와 air 를 분리하는 알고리즘
def check_air_position (start_point_x, start_point_y):
    deque = []
    deque.append([start_point_x,start_point_y])
    cheese_room[start_point_x][start_point_y] = 5
    move_x = [0,0,-1,1]
    move_y = [1,-1,0,0]
    while deque:
        temp = deque.pop(0)
        stay_x, stay_y = temp[0],temp[1]
        for i in range(4):
            moving_x = move_x[i] + stay_x
            moving_y = move_y[i] + stay_y

            if 0<= moving_x and moving_x < row and 0<= moving_y <colunm and cheese_room[moving_x][moving_y] == 0:
                cheese_room[moving_x][moving_y] = 5
                deque.append([moving_x,moving_y])

#  메인 코드


# 치즈 갯수 세는 코드
cheese_counter = 0
cheese_list = []
air_list = []
for i in range(row):
    for j in range(colunm):
        if cheese_room[i][j] ==1:
            cheese_list.append([i,j])
        else:
            air_list.append([i,j])
timer = 0
check_air_position(0,0)

# print(cheese_list)
q = []
change_list = []
trick_point = []
while cheese_list:
    temp = cheese_list.pop(0)
    now_x, now_y = temp[0], temp[1]
    move_x = [0, 0, -1, 1]
    move_y = [1, -1, 0, 0]
    count = 0

    for i in range(4):
        moving_x = move_x[i] + now_x
        moving_y = move_y[i] + now_y

        if cheese_room[moving_x][moving_y] == 5:
            count +=1
    if count >= 2:
        change_list.append([now_x,now_y])
    else:
        q.append([now_x,now_y])
    if len(cheese_list) == 0:
        timer +=1


        for tp in change_list:
            cheese_room[tp[0]][tp[1]] = 5
            for i in range(4):
                moving_x = move_x[i] + tp[0]
                moving_y = move_y[i] + tp[1]
                if cheese_room[moving_x][moving_y] == 0:
                    trick_point.append([moving_x, moving_y])

        while trick_point:
            trick_temp = trick_point.pop(0)
            check_air_position(trick_temp[0], trick_temp[1])

        cheese_list = cheese_list + q
        # 초기화
        q= []
        change_list = []
        trick_point = []


print(timer)
