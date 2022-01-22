import sys
sys.stdin = open('input.txt')


def dfs(start, num_index, cal_index):
    global min, max, N

    if cal_index == N-1 :
        if min > start:
            min = start
        if max < start:
            max = start
        return

    for i in range(N-1):
        if visited[i] == 1:
            continue
        else:
            visited[i] = 1
            if cal_list[i] == 1:
                start = start + num_list[num_index]
                cal_index += 1
                dfs(start, num_index + 1, cal_index)
                start = start - num_list[num_index]
            elif cal_list[i] == 2:
                start = start - num_list[num_index]
                cal_index += 1
                dfs(start, num_index + 1, cal_index)
                start = start + num_list[num_index]

            elif cal_list[i] == 3:
                start = start * num_list[num_index]
                cal_index += 1
                dfs(start, num_index + 1, cal_index)
                start = int(start / num_list[num_index])

            elif cal_list[i] == 4:
                start = int(start / num_list[num_index])
                cal_index += 1
                dfs(start, num_index + 1, cal_index)
                start = start * num_list[num_index]

            visited[i] = 0
            cal_index -= 1


T= int(input())

for tc in range(1,T+1):
    N = int(input()) # 수의 개수
    num_list = list(map(int, input().split()))
    index_list = list(map(int, input().split()))
    cal_list = []
    visited = [0] * (N-1)
    min = 9999999999999999
    max = -9999999999999999
    # 연산자를 각각 숫자로 하여 넣어줌
    for i in range(len(index_list)):
        for j in range(index_list[i]):
            cal_list.append(i+1)

    dfs(num_list[0],1,0)
    print(max, min)
