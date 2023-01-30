import sys

sys.stdin = open('input.txt')

T = int(input())

def rotate(x,y,an,rotate_num):
    global temp
    if an == 0:
        temp = [x, y-1,3,rotate_num]
    elif an ==1:
        temp = [x-1, y,0,rotate_num]
    elif an ==2:
        temp = [x, y+1,1,rotate_num]
    elif an == 3:
        temp = [x+1, y,2,rotate_num]

    if clean_map[temp[0]][temp[1]] == 0:
        return (temp)
    else:
        rotate_temp = temp[2]
        temps = [x , y, rotate_temp, rotate_num+1]
        return (temps)

def Diririri(x,y,an):
    global temp,cant_go_back
    if an == 0:
        temp = [x + 1, y, an]
    elif an == 1:
        temp = [x , y-1, an]
    elif an == 2:
        temp = [x-1, y, an]
    elif an == 3:
        temp = [x, y+1, an]

    # 만약 후진을 못하면...?
    if clean_map[temp[0]][temp[1]] == 1:
        cant_go_back = 1
        return (temp)
    else:
        return (temp)


for tc in range(T):
    n,m = map(int, input().split())
    x, y, A = map(int, input().split())
    clean_map = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        clean_map.append(temp)
    rotate_num = 0
    cant_go_back = 0
    result_clean = 0
    while cant_go_back == 0:
        if clean_map[x][y] == 0:
            clean_map[x][y] = 5
            result_clean +=1
            rotate_num = 0
        al_temp = rotate(x,y,A,rotate_num)
        x,y,A,rotate_num = al_temp[0],al_temp[1],al_temp[2],al_temp[3]

        if rotate_num >=4:
            #후진을 한다
            x, y, A =  Diririri(x,y,A)
            rotate_num =0



    print(result_clean)