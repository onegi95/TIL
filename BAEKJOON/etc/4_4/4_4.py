def game():
    pass

import sys
from typing import Counter
sys.stdin = open('input.txt')
n, m = map(int, input().split())

player_x , player_y , view_point = map(int, input().split())

game_map = []
for i in range(n):
    game_map.append( list(map(int, input().split())))

way_count = 1
break_count = 0
# 캐릭터를 이동시킨다
while break_count <4:
    if view_point == 0: # 북쪽을 볼 때
        if game_map[player_y][player_x-1] == 0:
            view_point += 3
            player_x -= 1 # 이동에 성공하면
            game_map[player_y][player_x] = 1 # 이동한 부분을 색칠하고
            way_count += 1
            break_count = 0 # 브레이크 포인트 초기화
        else:
            view_point += 3
            break_count += 1 
    if view_point == 1: # 동쪽을 볼 때
        if game_map[player_y-1][player_x] == 0:
            view_point -= 1
            player_y -= 1 # 이동에 성공하면
            game_map[player_y][player_x] = 1 # 이동한 부분을 색칠하고
            way_count += 1
            break_count = 0 # 브레이크 포인트 초기화
        else:
            view_point -= 1
            break_count += 1 
    if view_point == 2: # 남쪽을 볼 때
        if game_map[player_y][player_x+1] == 0:
            view_point -= 1
            player_x += 1 # 이동에 성공하면
            game_map[player_y][player_x]  = 1 # 이동한 부분을 색칠하고
            way_count += 1
            break_count = 0 # 브레이크 포인트 초기화
        else:
            view_point -= 1
            break_count += 1 
    if view_point == 3: # 서쪽을 볼 때
        if game_map[player_y+1][player_x] == 0:
            view_point -= 1
            player_y += 1 # 이동에 성공하면
            game_map[player_y][player_x] = 1 # 이동한 부분을 색칠하고
            way_count += 1
            break_count = 0 # 브레이크 포인트 초기화
        else:
            view_point -= 1
            break_count += 1 

print(way_count)