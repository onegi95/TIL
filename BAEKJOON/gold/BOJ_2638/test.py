import sys
sys.stdin = open('input.txt')

row, colunm = map(int, input().split())

cheese_room = []
for _ in range(row):
    cheese_room.append(list(map(int, input().split())))

# blank 와 air 를 분리하는 알고리즘
def check_air_position (start_point_x, start_point_y):
    global row, colunm
    pop_list = []
    pop_list.append([start_point_x,start_point_y])
    while pop_list:
        point_list = pop_list.pop()
        cheese_room[point_list[0]][point_list[1]] = 5
        x_position = [0,0,1,-1]
        y_position = [1,-1,0,0]
        for i in range(4):
            move_point_x = point_list[0] + x_position[i]
            move_point_y = point_list[1] + y_position[i]
            if 0<= move_point_x and move_point_x < row and 0<=move_point_y and move_point_y <colunm and cheese_room[move_point_x][move_point_y] != 1 and cheese_room[move_point_x][move_point_y] != 5:
                pop_list.append([move_point_x,move_point_y])
#  앞으로 썩을 치즈를 찾아내는 알고리즘
def detect_rotten_cheese(start_point_x,start_point_y):
    # 이걸 최초 listup 해서 가져오도록 하자(치즈의 위치를)
    # blank 도 없을경우 => 실행안함 프로세스를 가지면 시간 절약 될 듯!
    # 즉 blank 위치파악이 중요
    global  row, column,cheese_list
    detected_list = []
    for _ in range(len(cheese_list)):
        counter = 0
        i,j = cheese_list[0], cheese_list[1]
        x_position = [0, 0, 1, -1]
        y_position = [1, -1, 0, 0]
        for t in range(4):
            move_point_x = i + x_position[t]
            move_point_y = j + y_position[t]
            if 0 <= move_point_x and move_point_x < row and 0 <= move_point_y and move_point_y < colunm and cheese_room[move_point_x][move_point_y]==5:
                counter+=1
        if counter >=2:
            detected_list.append([i,j])

    return detected_list


#  메인 코드

# 치즈 갯수 세는 코드
cheese_counter = 0
cheese_list = []
for i in range(row):
    for j in range(colunm):
        if cheese_room[i][j] ==1:
            cheese_list.append([i,j])
timer = 0
#  메인 알고리즘
while cheese_list:
    check_air_position(0,0)
    find_cheese = detect_rotten_cheese(0,0)
    cheese_list.remove(find_cheese)
    for i in range(len(find_cheese)):
        cheese_room[find_cheese[i][0]][find_cheese[i][1]] = 5
    timer +=1

print(timer)


