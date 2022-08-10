import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    line_index = int(input())
    all_list = []
    all_list.append(list(map(int, input().split())))
    all_list.append(list(map(int, input().split())))
    summy1 = 0
    summy2 = 0
    index_place = 0

    point1 = 0
    point2 = 1

    def find_max_point(startP):
        summy = 0
        index_place = 0
        while True:
            # start point = 0
            summy += all_list[startP][index_place]
            if index_place + 3 == line_index:
                if startP == 0:
                    if all_list[1][index_place + 1] + all_list[0][index_place + 2] > all_list[1][index_place + 2]:
                        summy += (all_list[1][index_place + 1] + all_list[0][index_place + 2])
                    else:
                        summy += all_list[1][index_place + 2]
                else:
                    if all_list[0][index_place + 1] + all_list[1][index_place + 2] > all_list[0][index_place + 2]:
                        summy += (all_list[0][index_place + 1] + all_list[1][index_place + 2])
                    else:
                        summy += all_list[0][index_place + 2]
                break
            if index_place + 2 == line_index:
                if startP == 0:
                    summy += (all_list[1][index_place + 1])
                else:
                    summy += all_list[0][index_place + 1]
                break

            if startP == 0:
                if all_list[1][index_place + 1] + all_list[0][index_place + 2] > all_list[1][index_place + 2]:
                    index_place += 1
                    startP = 1
                else:
                    index_place += 2
                    startP = 1
            else:
                if all_list[0][index_place + 1] + all_list[1][index_place + 2] > all_list[0][index_place + 2]:
                    index_place += 1
                    startP = 0
                else:
                    index_place += 2
                    startP = 0

        return  summy

    print(max(find_max_point(0),find_max_point(1)))
    
    
    
    #  안되는 이유? => 뒷쪽 상황에서 에러가 발생할 수 있음! 앞에서 부터 차근차근 가는것을 목표하자

    t = int(input())
    for i in range(t):
        s = []
        n = int(input())
        for k in range(2):
            s.append(list(map(int, input().split())))
        for j in range(1, n):
            if j == 1:
                s[0][j] += s[1][j - 1]
                s[1][j] += s[0][j - 1]
            else:
                s[0][j] += max(s[1][j - 1], s[1][j - 2])
                s[1][j] += max(s[0][j - 1], s[0][j - 2])
        print(max(s[0][n - 1], s[1][n - 1]))

    #  코드 보면서 복습할 것