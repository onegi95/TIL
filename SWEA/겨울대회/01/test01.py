import sys
sys.stdin = open('input.txt')

T = int(input())

def search(start, deep):
    global min_deep
    if abs(start[0] - end_point[0]) + abs(start[1] - end_point[1]) <= L:
        min_deep = min(min_deep , deep)
        return
    else:
        for an in anchor_point:
            if an not in visited and abs(start[0] - an[0]) + abs(start[1] - an[1]) <= L:
                visited.append(an)
                search(an,deep+1)
                visited.remove(an)




for tc in range(1,T+1):
    M,N,L = map(int, input().split()) # 행 열 길이

    map_list = []
    for i in range(M):
        temp = list(map(int, input().split()))
        map_list.append(temp)

    anchor_point = []
    for i in range(M):
        for j in range(N):
            if map_list[i][j] != 0:
                if map_list[i][j] == 1:
                    anchor_point.append([i,j])
                elif map_list[i][j] == 2:
                    start_point=[i,j]
                elif map_list[i][j] == 3:
                    end_point =[i,j]
    min_deep = 10000000
    visited = []

    search(start_point,0)

    if min_deep == 10000000:
        print('#{} {}'.format(tc,-1))
    else:
        print('#{} {}'.format(tc,min_deep))