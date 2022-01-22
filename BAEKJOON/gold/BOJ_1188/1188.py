import sys
sys.stdin = open('input.txt')

meet, pp = map(int, input().split())

if meet % pp == 0:
    print(0)

else:
    if pp % meet == 0:
        pp = pp//meet
        meet = 1

    while meet % 3 == 0 and meet // 3 != 0 and pp % 3 == 0 and pp // 3 != 0:
        meet = meet//3
        pp = pp//3
    while meet % 3 == 0 and meet // 3 != 0 and pp % 3 == 0 and pp // 3 != 0:
        meet = meet//3
        pp = pp//3
print( meet, pp)