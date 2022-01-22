import sys
sys.stdin = open('test_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    DAY, Max, target_hmd = map(int,input().split())

    hmd_list = []
    for i in range(DAY):
        hmd_list.append(int(input()))

    idx = 0
    anw_list = []
    while True:
        drum = 0
        first_day = idx +1
        while drum < Max:
            if idx == DAY:
                break
            drum += (target_hmd - hmd_list[idx])
            if drum <= Max:
                idx += 1
                pass
            else:
                drum -= (target_hmd - hmd_list[idx])
                break

        anw_list.append([first_day,drum])
        if idx == DAY:
            break

    print(tc, anw_list)


