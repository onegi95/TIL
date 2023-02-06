import sys
sys.stdin = open('input.txt')
# 가로세로 인풋(가세연 아님)
N, M = map(int, input().split())

T = int(input())

anw = 0
# gd,gl = 가드의 방향, 거리
# td,tl = 타깃의 방향, 거리
def no1(gd,gl,td,tl):
    # 둘의 방향이 같을 경우
    # 북남서동
    if gd == td:
        temp = abs(gl-tl)
        return temp
    elif gd ==1 :
        # 맞은편
        if td == 2:
            temp = M + min((2*N -gl - tl), (gl+tl))
            return temp
        elif td ==3:
            temp = gl + +tl
            return temp
        else:
            temp = N - gl + M - tl
            return temp
        # 북남서동
    elif gd ==2 :
        if td == 1:
            temp = M + min((2*N -gl - tl), (gl+tl))
            return temp
        elif td ==3:
            temp = gl + M - tl
            return temp
        else:
            temp = N-gl + M - tl
            return temp
        # 북남서동
    elif gd ==3 :
        if td == 4:
            temp = N + min((2*M -gl - tl), (gl+tl))
            return temp
        elif td ==1:
            temp = gl + tl
            return temp
        else:
            temp = M - gl + tl
            return temp

    else:
        if td == 3:
            temp = N+ min((2*M -gl - tl), (gl+tl))
            return temp
        elif td ==1:
            temp = gl + N - tl
            return temp
        else:
            temp = N - gl + M - tl
            return temp




check = []
for i in range(T):
    a, b = map(int, input().split())
    check.append([a,b])
d1,d2= map(int, input().split())

anw = 0
for ch in check:
    anw += no1(d1,d2,ch[0],ch[1])

print(anw)