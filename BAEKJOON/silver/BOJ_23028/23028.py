import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(T):
    goal_sum = 130
    goal_major = 66

    passed, major, total = map(int, input().split(' '))
    point_array  = []
    for _ in range(10):
        point_array.append(list(map(int, input().split())))

    left_time = 8-passed

    left_point_array = point_array[0:left_time]

    major_point = 0
    all_point = 0
    for i in range(len(left_point_array)):
        if left_point_array[i][0] <= 6:
            major_point += left_point_array[i][0]
        else:
            major_point += 6
        if left_point_array[i][0] + left_point_array[i][1] <=6:
            all_point += (left_point_array[i][0] + left_point_array[i][1])
        else:
            all_point += 6
    if (( major_point)*3) + major >= goal_major and (all_point)*3 + total >= goal_sum:
        print("Nice")
    else:
        print('Nae ga wae')