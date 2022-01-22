import sys
sys.stdin = open('input.txt')

T= int(input())


# dfs 로 cctv 위치 확인
def dfs(map, count):
    global anw, temp
    if temp == 1:
        return
    if count == 0:
        anw = 0
        search()
        if anw == 0:
            temp = 1
        return
    for i in range(len(cctv_list)):
        if temp == 1:
            break
        if visited[cctv_list[i][0]][cctv_list[i][1]] == 1:
            continue
        else:
            visited[cctv_list[i][0]][cctv_list[i][1]] = 1
            cl_map[cctv_list[i][0]][cctv_list[i][1]] = 'B'
            dfs(map, count - 1)
            cl_map[cctv_list[i][0]][cctv_list[i][1]] = 'X'
            visited[cctv_list[i][0]][cctv_list[i][1]] = 0


# teacher 로부터 4방향으로 탐색해서 걸리는지 확인인
def search():
    global anw, temp

    for i in range(len(teacher_list)):
        if anw == 1:
            break
        teacher_place_x = teacher_list[i][1]
        teacher_place_y = teacher_list[i][0]
        while 0 <= teacher_place_x < N and 0 <= teacher_place_y < N :
            if cl_map[teacher_place_y][teacher_place_x] == 'S':
                anw = 1
                break
            if cl_map[teacher_place_y][teacher_place_x] == 'B':
                break
            teacher_place_y += 1

        teacher_place_x = teacher_list[i][1]
        teacher_place_y = teacher_list[i][0]
        while 0 <= teacher_place_x < N and 0 <= teacher_place_y < N:
            if cl_map[teacher_place_y][teacher_place_x] == 'S':
                anw = 1
                break
            if cl_map[teacher_place_y][teacher_place_x] == 'B':
                break
            teacher_place_y -= 1

        teacher_place_x = teacher_list[i][1]
        teacher_place_y = teacher_list[i][0]
        while 0 <= teacher_place_x < N and 0 <= teacher_place_y < N:
            if cl_map[teacher_place_y][teacher_place_x] == 'S':
                anw = 1
                break
            if cl_map[teacher_place_y][teacher_place_x] == 'B':
                break
            teacher_place_x += 1

        teacher_place_x = teacher_list[i][1]
        teacher_place_y = teacher_list[i][0]
        while 0 <= teacher_place_x < N and 0 <= teacher_place_y < N:
            if cl_map[teacher_place_y][teacher_place_x] == 'S':
                anw = 1
                break
            if cl_map[teacher_place_y][teacher_place_x] == 'B':
                break
            teacher_place_x -= 1



for tc in range(1,T+1):
    temp = 0
    N = int(input()) # 수의 개수
    cl_map = []
    for i in range(N):
        cl_map.append(list(input().split()))

    teacher_list = []
    student_list =  []
    cctv_list = []
    for i in range(N):
        for j in range(N):
            if cl_map[i][j] == 'X':
                cctv_list.append([i,j])
            elif cl_map[i][j] == 'T':
                teacher_list.append([i,j])
            else:
                student_list.append([i,j])
    visited = [([0]*N )for _ in range(N)]
    anw = 0
    dfs(cl_map,3)
    if temp == 1:
        print('YES')
    else:
        print('NO')






