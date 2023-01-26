import sys
sys.stdin = open('input.txt')

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


#  앞으로 썩을 치즈를 찾아내는 알고리즘 (blank가 있을때)
def detect_rotten_cheese():
    global anw
    move_x = [0, 0, -1, 1]
    move_y = [1, -1, 0, 0]
    while cheese_list:
        triger = 0
        for target in cheese_list:
            x,y = target[0],target[1]
            temp_score = 0

            for i in range(4):
                moving_x = move_x[i] + x
                moving_y = move_y[i] + y
                if 0 <= moving_x and moving_x < row and 0 <= moving_y < colunm and cheese_room[moving_x][moving_y] == 5:
                    temp_score +=1
                elif 0 <= moving_x and moving_x < row and 0 <= moving_y < colunm and cheese_room[moving_x][moving_y] == 0:  # 블랭크를 발견할 경우
                    triger = 1
            if temp_score >= 2 :
                cheese_room[x][y] = 5
        if triger == 1:
            check_air_position(0,0)

        anw +=1
#  앞으로 썩을 치즈를 찾아내는 알고리즘 (blank가 없을때)
def detect_rotten_cheese_noblank(start_point_x, start_point_y):
    pass

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
for i in range(len(cheese_room)):
    print(cheese_room[i])

detect_rotten_cheese()
#  메인 알고리즘

print(anw)