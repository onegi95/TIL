import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1,N+1):
    number = list(map(int, input()))
    check = 1
    for i in range(len(number)):
        if number[i] == 0:
            continue
        elif number[i] == 1:
            check = check+number[i]
        else:
            check = check*number[i]

    print(check)