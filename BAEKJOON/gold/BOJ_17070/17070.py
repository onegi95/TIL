import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    #  초기셋팅
    N = int(input())

    pipe_map = []

    for _ in range(N):
        temp = list(map(int, input().split()))
        pipe_map.append(temp)

    dp_map = [[0 for _ in range(N)]for _ in range(N)]

    #  방향에 대한 불용 죄표 확인하기
    #  방향이 바뀌명 => 엥글을 따로 바꿔 줘야 함
    #  즉 가는 방향마다 최소로 갈 수 있는 값을 정해주는 것
    #  만약 갱신할 수 없는 상황이라면 => 0출력