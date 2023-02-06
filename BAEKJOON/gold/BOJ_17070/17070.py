import sys
import queue
sys.stdin = open('input.txt')
input = sys.stdin.readline
T = int(input())

for tc in range(T):
    #  초기셋팅
    N = int(input())

    pipe_map = []

    for _ in range(N):
        temp = list(map(int, input().split()))
        pipe_map.append(temp)
    anw = 0
    def dfs(x,y,d):
        global anw

        if x == N-1 and y == N-1:
            anw += 1
            return
        # 가로로 가는 경우
        if d == 1 or d == 3:
            if y + 1 <N and pipe_map[x][y+1] == 0:
                dfs(x,y+1,1)
        # 방향이 세로일 경우
        if d == 2 or d == 3:
            if x+1 < N and  pipe_map[x+1][y] == 0:
                dfs(x+1,y,2)
        #  방향이 대각선일 경우
        if x+1 < N and y+1 < N:
            if  pipe_map[x][y+1] == 0 and  pipe_map[x+1][y] == 0 and  pipe_map[x+1][y+1] == 0 :
                dfs(x+1,y+1,3)


    dfs(0,1,1)
    print(anw)
    # dp_map = [[0 for _ in range(N)]for _ in range(N)]
    #
    # #  방향에 대한 불용 죄표 확인하기
    # #  각 result 에는 갈 수 있는방향과 방향당 최종 봐표, 비워져야 하는 좌표가 정해져 있음.
    # def garo(x,y):
    # #     2개의 가능성을 줘야 함
    #     result = []
    #     if x < N and y+1 <N:
    #         garo = [x,y+1,[[x,y+1]],1]
    #         result.append(garo)
    #     if x +1 < N and y+1 <N:
    #         daegack = [x+1, y+1, [[x+1,y+1],[x,y+1],[x+1,y]],3]
    #         result.append(daegack)
    #     return result
    # def sero(x,y):
    #     result = []
    #     if x +1< N and y <N:
    #         sero = [x+1,y,[[x+1,y]],2]
    #         result.append(sero)
    #     if x +1 < N and y+1 <N:
    #         daegack = [x+1, y+1, [[x+1,y+1],[x,y+1],[x+1,y]],3]
    #         result.append(daegack)
    #     return result
    #
    # def deagack(x,y):
    #     result = []
    #     if x < N and y+1 <N:
    #         garo = [x,y+1,[[x,y+1]],1]
    #         result.append(garo)
    #     if x +1< N and y <N:
    #         sero = [x+1,y,[[x+1,y]],2]
    #         result.append(sero)
    #     if x +1 < N and y+1 <N:
    #         daegack = [x+1, y+1, [[x+1,y+1],[x,y+1],[x+1,y]],3]
    #         result.append(daegack)
    #     return result
    #
    # # 방향의 스테이터스, 1=가로 2=세로 3=대각선
    # status = 1
    # heap=[]
    # # 초기 좌표 설정
    # heap.append([0,1,[],1])
    #
    # while heap:
    #     temp = heap.pop(0)
    #     if temp[3] == 1:
    #         # heap에서 자료를 가져옴
    #         x,y = temp[0],temp[1]
    #         result = garo(x,y)
    #         for re in result:
    #             break_point = 0
    #             for section in re[2]:
    #                 if section[0] < N and section[1] < N and pipe_map[section[0]][section[1]] == 0:
    #                     pass
    #                 else:
    #                     break_point = 1
    #             if break_point == 1:
    #                 pass
    #             else:
    #                 if re[0] < N and re[1] < N :
    #                     dp_map[re[0]][re[1]] +=1
    #                     heap.append([re[0], re[1], re[2], re[3]])
    #
    #
    #     elif temp[3] ==2:
    #
    #         # heap에서 자료를 가져옴
    #         x, y = temp[0], temp[1]
    #         result = sero(x, y)
    #         for re in result:
    #             break_point = 0
    #             for section in re[2]:
    #                 if section[0] < N and section[1] < N and pipe_map[section[0]][section[1]] == 0:
    #                     pass
    #                 else:
    #                     break_point = 1
    #             if break_point == 1:
    #                 pass
    #             else:
    #                 if re[0] < N and re[1] < N :
    #                     dp_map[re[0]][re[1]] +=1
    #                     heap.append([re[0], re[1], re[2], re[3]])
    #
    #
    #     else:
    #         x, y = temp[0], temp[1]
    #         result = deagack(x, y)
    #         for re in result:
    #             break_point = 0
    #             for section in re[2]:
    #                 if section[0] < N and section[1] < N and pipe_map[section[0]][section[1]] == 0:
    #                     pass
    #                 else:
    #                     break_point = 1
    #             if break_point == 1:
    #                 pass
    #             else:
    #                 if re[0] < N and re[1] < N :
    #                     dp_map[re[0]][re[1]] +=1
    #                     heap.append([re[0], re[1], re[2], re[3]])
    #
    # print(dp_map[N-1][N-1])
    # #  방향이 바뀌명 => 엥글을 따로 바꿔 줘야 함
    # #  즉 가는 방향마다 최소로 갈 수 있는 값을 정해주는 것
    # #  만약 갱신할 수 없는 상황이라면 => 0출력
