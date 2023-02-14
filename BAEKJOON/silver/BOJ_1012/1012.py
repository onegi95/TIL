import sys
sys.stdin = open('input.txt')

T = int(input())


def bfs(x,y):
    x, y = temp[0], temp[1]

    q = []
    q.append([x,y])
    while q:
        qtemp = q.pop(0)
        qx,qy = qtemp[0], qtemp[1]
        if visit_list[qx][qy] == 1:
            continue
        else:
            visit_list[qx][qy] = 1
            move_x = [0, 0, -1, 1]
            move_y = [1, -1, 0, 0]
            for i in range(4):
                moving_x = qx + move_x[i]
                moving_y = qy + move_y[i]

                if moving_x >= 0 and moving_x < N and moving_y < M and moving_y >= 0:
                    if baechu_map[moving_x][moving_y] == 1 and visit_list[moving_x][moving_y] == 0:
                        q.append([moving_x,moving_y])



for tc in range(T):
    anw = 0
    M, N ,K = map(int, input().split())

    visit_list = [[0 for _ in range(M+1)] for _ in range(N+1)]

    baechu_map = [[0 for _ in range(M+1)] for _ in range(N+1)]

    baechu_list = []

    for i in range(K):
        a,b = map(int, input().split())
        baechu_map[b][a] = 1
        baechu_list.append([b,a])
    q = []
    while baechu_list:
        temp = baechu_list.pop(0)
        now_x,now_y = temp[0],temp[1]
        if visit_list[now_x][now_y] == 1:
            continue
        else:
            anw += 1
            bfs(now_x,now_y)
    print(anw)




