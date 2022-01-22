import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1,T+1):
    N= int(input())

    num_list = list(map(int, input().split()))

    start = 0
    end = N-1
    anw = -1
    while True:
        if start == end:
            break

        center = (start + end) //2

        if num_list[center] == center:
            anw = center
            break
        if num_list[center] < 0:
            if start == center:
                start = center +1
                continue
            start = center
            end = end
            continue
        if num_list[center] < center:
            start = center
            end = end
            continue
        if num_list[center] > center:
            end = center
            start = start
            continue
    print(anw)
