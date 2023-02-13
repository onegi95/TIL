import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(T):
    a,b,c= map(int, input().split())
    chess_box = []
    w = 0
    b = 0
    for _ in range(row):
        temp = str(input())
        for i in temp:
            if i == 'W':
                w +=1
            else:
                b +=1
    print(abs(w-b)//2)




#  전방위 탐색을 해봐야 겠다