import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    X = int(input())
    if 64//X ==0:
        print(1)
    else:
        stick_len = 64
