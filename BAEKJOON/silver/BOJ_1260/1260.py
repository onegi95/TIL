import sys
sys.stdin = open('input.txt')

def DFS(start_point):
    if start_point not in DFS_list:
        DFS_list.append(start_point)
        for i in range(len(nord_list[start_point])):
            DFS(nord_list[start_point][i])
    return


def BFS(start_point):
    BFS_list.append(start_point)
    BFS_stack.append(start_point)
    while BFS_stack:
        a = BFS_stack.pop(0)
        for i in range(len(nord_list[a])):
            if nord_list[a][i] not in BFS_list:
                BFS_stack.append(nord_list[a][i])
                BFS_list.append(nord_list[a][i])
    return




T = int(input())

for tc in range(1,T+1):
    N,M,V = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수, 시작하는 정점

    # 빈 노드
    nord_list = [[] for _ in range(N+1)]
    for i in range(M):
        temp = list(map(int, input().split()))
        nord_list[temp[0]].append(temp[1])
        nord_list[temp[1]].append(temp[0])

    for i in range(len(nord_list)):
        nord_list[i].sort()

    DFS_list = []
    BFS_list = []
    BFS_stack = []

    BFS(V)
    DFS(V)

    print(" ".join(map(str,DFS_list)))
    print(" ".join(map(str, BFS_list)))