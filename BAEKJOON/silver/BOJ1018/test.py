import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(T):
    row, column = map(int, input().split())
    chess_box = []
    for _ in range(row):
        temp = (input())
        chess_box.append(temp)
    anw = 1000000000000000000000000
    for r in range(row):
        for c in range(column):
            if c+8 <= column and r +8 <= row:
                for c1 in range(c,c+8):
                    for r1 in range(r,r+8):
                        if chess_box[r1][c1]  == 'W':

    print(int(anw))


#  전방위 탐색을 해봐야 겠다