import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 맵의 크기
    num_apple = int(input()) # 사과의 갯수

    # 맵 만들기
    apple_map = [([0]*N) for _ in range(N)]

    # 사과 위치 정하기
    for _ in range(num_apple):
        x, y = map(int, input().split())
        apple_map[x-1][y-1] = 1

    # 방향 변환 횟수
    change_dir = int(input())

    # 방향 변환 스택
    dir_time = []
    dir_way = []
    for _ in range(change_dir):
        x, y = map(str, input().split())
        dir_time.append(int(x))
        dir_way.append(y)

    dir_stack = [0] * (max(dir_time)+1)
    for i in range(change_dir):
        dir_stack[dir_time[i]] = dir_way[i]

    # 최초 방향 백터
    direction = 0

    # 최초 뱀의 위치
    head = [0,0]
    # 뱀의 전체 길이
    body = []
    x, y = head[0], head[1]
    body.append([x,y])
    time = 0
    apple_map[head[0]][head[1]] = 2
    while True:
        time += 1
        # 동쪽으로 이동할 경우
        if direction == 0:
            head[1] += 1 # 헤드를 이동해 주고
            # 종료조건을 준다
            if head[0]<0 or head[0] >= N or head[1]<0 or head[1] >= N:
                break
            # 만약 자기 자신을 만났다면?
            if apple_map[head[0]][head[1]] == 2: # 끝 꼬리가 아니었다면
                break
            # 종료조건을 피해 왔다면, 머리를 추가해주자
            # 사과가 있었다면?
            if apple_map[head[0]][head[1]] == 1:
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
            else: # 사과가 없으면? 꼬리를 자르자
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
                temp = body.pop(0)
                apple_map[temp[0]][temp[1]] = 0





        # 서쪽으로 이동할 경우
        if direction == 2:
            head[1] -= 1 # 헤드를 이동해 주고
            # 종료조건을 준다
            if head[0]<0 or head[0] >= N or head[1]<0 or head[1] >= N:
                break
            # 만약 자기 자신을 만났다면?
            if apple_map[head[0]][head[1]] == 2 : # 끝 꼬리가 아니었다면
                break
            # 종료조건을 피해 왔다면, 머리를 추가해주자
            # 사과가 있었다면?
            if apple_map[head[0]][head[1]] == 1:
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
            else: # 사과가 없으면? 꼬리를 자르자
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
                temp = body.pop(0)
                apple_map[temp[0]][temp[1]] = 0

        # 북쪽으로 이동할 경우
        if direction == 3:
            head[0] -= 1 # 헤드를 이동해 주고
            # 종료조건을 준다
            if head[0]<0 or head[0] >= N or head[1]<0 or head[1] >= N:
                break
            # 만약 자기 자신을 만났다면?
            if apple_map[head[0]][head[1]] == 2 : # 끝 꼬리가 아니었다면
                break
            # 종료조건을 피해 왔다면, 머리를 추가해주자
            # 사과가 있었다면?
            if apple_map[head[0]][head[1]] == 1:
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
            else: # 사과가 없으면? 꼬리를 자르자
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
                temp = body.pop(0)
                apple_map[temp[0]][temp[1]] = 0

        # 남쪽으로 이동할 경우
        if direction == 1:
            head[0] += 1 # 헤드를 이동해 주고
            # 종료조건을 준다
            if head[0]<0 or head[0] >= N or head[1]<0 or head[1] >= N:
                break
            # 만약 자기 자신을 만났다면?
            if apple_map[head[0]][head[1]] == 2: # 끝 꼬리가 아니었다면
                break
            # 종료조건을 피해 왔다면, 머리를 추가해주자
            # 사과가 있었다면?
            if apple_map[head[0]][head[1]] == 1:
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
            else: # 사과가 없으면? 꼬리를 자르자
                apple_map[head[0]][head[1]] = 2
                x, y = head[0], head[1]
                body.append([x, y])
                temp = body.pop(0)
                apple_map[temp[0]][temp[1]] = 0

        if time <= max(dir_time) and dir_stack[time] :
            if dir_stack[time] == 'D':
                direction += 1
                if direction == 4:
                    direction = 0

            elif dir_stack[time] == 'L':
                direction -= 1
                if direction == -1:
                    direction = 3


    print('#{} {}'.format(tc, time))
