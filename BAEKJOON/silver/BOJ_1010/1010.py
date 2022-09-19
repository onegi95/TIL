import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    west,east = map(int,input().split(' '))
    temp = east
    sol_west = west
    sol_east = east
    stemp = 1
    while temp != (east -west+1):
        temp -= 1
        sol_east = sol_east * (east-stemp)
        sol_west = sol_west * (west-stemp)
        stemp += 1

    print(int(sol_east/sol_west))