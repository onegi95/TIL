import sys

sys.stdin = open('input.txt')

T = int(input())

def rotate(x,y,an):
    if an == 0:
        temp = [x, y-1,3]
        return (temp)
    elif an ==1:
        temp = [x-1, y,0]
        return (temp)
    elif an ==2:
        temp = [x, y+1,1]
        return (temp)
    else:
        temp = [x+1, y,2]
        return (temp)

for tc in range(T):
    n,m = map(int, input().split())
    x, y, A = map(int, input().split())
    clean_map = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        clean_map.append(temp)
    rotate_num = 0
    result_clean = 0
    while rotate_num <=5:
        if clean_map[x][y] == 0:
            clean_map[x][y] = 5
            result_clean +=1
            temp = rotate(x,y,A)
            x,y,A = temp[0],temp[1],temp[2]
        else:
            temp = rotate(x, y, A)
            x, y, A = temp[0], temp[1], temp[2]
            rotate_num +=1

    print(result_clean)