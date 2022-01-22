import sys
sys.stdin = open('input.txt')

food_time = list(map(int, input().split()))
k = int(input())

sum_food = sum(food_time)
what_eat = 0
time = 0
while sum(food_time)>0:
    # 음식을 다시 돌아와서 먹는 루틴

    # 먹을 음식이 0 이면? 넘겨~
    while food_time[what_eat] == 0:
        what_eat +=1
    
    if what_eat >= len(food_time):
        what_eat = what_eat-len(food_time)
    
    food_time[what_eat] -= 1
    what_eat += 1
    time += 1
    if what_eat >= len(food_time):
        what_eat = what_eat-len(food_time)
    # 방송을 멈출 시간이 되면?
    if time == k:
        break

if sum(food_time) == 0:
    print(-1)
else:
    while food_time[what_eat] == 0:
        what_eat +=1
    print(what_eat+1)