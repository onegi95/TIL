import sys
sys.stdin = open('input.txt')

def find_num(start,end,tg):
    global right, left
    if start == end:
        return
    center = (start + end) //2
    if num_list[center] == tg and num_list[center+1] != tg:
        # 양 옆으로 뛰어 본다
        right = center + 1
    elif num_list[center] == tg and num_list[center-1] != tg:
        # 양 옆으로 뛰어 본다
        left = center - 1
    # 만약 타겟이라면?
    elif num_list[center] == tg :
        # 양 옆으로 뛰어 본다
        find_num(start,center,tg)
        find_num(center+1,end,tg)

    # 경계에 잡힌 경우
    elif num_list[center] < tg and num_list[center+1] == tg: # 왼쪽에서 잡혔으면?
        left = center +1
        return
    elif num_list[center] > tg and num_list[center-1] == tg:
        right = center-1
        return

    # 왼 오 가보자
    if num_list[center] < tg:
        find_num(center+1,end,tg)
    elif num_list[center] > tg:
        find_num(start,center,tg)

T = int(input())

for tc in range(1,T+1):
    N, target = map(int, input().split())

    num_list = list(map(int, input().split()))

    right = 0
    left = 0

    find_num(0,N-1,target)

    if right - left == 0:
        print(-1)
    else:
        print(right-left)