import sys
sys.stdin = open('input.txt')

N = int(input()) # 맵의 크기
move_list = list((input().split()))
start_point_x = 1
start_point_y = 1
# 움직임을 만들어 주자
for i in range(len(move_list)):
    if move_list[i] == 'R': # 오른쪽으로 간다고 하면?
        if start_point_x + 1 <=N:
            start_point_x += 1

    if move_list[i] == 'L': # 왼쪽으로 간다고 하면?
        if start_point_x - 1 >= 1:
            start_point_x -= 1
            
    if move_list[i] == 'U': # 위쪽으로 간다고 하면?
        if start_point_y - 1 >= 1:
            start_point_y -= 1
    
    if move_list[i] == 'D': # 아래쪽으로 간다고 하면?
        if start_point_y + 1 <= N:
            start_point_y += 1

print(start_point_y,start_point_x)

