import sys
sys.stdin = open('input.txt')



def search(x,y,target):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    color_list[x][y] = 'X'
    stack = [[x,y]]
    while stack:
        temps = stack.pop(0)
        rx = temps[0]
        ry = temps[1]
        for t in range(4):
            gox = rx + dx[t]
            goy = ry + dy[t]
            if  0<= gox < N and 0<= goy < N and color_list[gox][goy] == target :
                color_list[gox][goy] = 'X'
                stack.append([gox,goy])

    return


def bd_search(x,y,target):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    bd_color_list[x][y] = 'X'
    stack = [[x,y]]
    while stack:
        temps = stack.pop(0)
        rx = temps[0]
        ry = temps[1]
        for t in range(4):
            gox = rx + dx[t]
            goy = ry + dy[t]
            if  0<= gox < N and 0<= goy < N and bd_color_list[gox][goy] == target :
                bd_color_list[gox][goy] = 'X'
                stack.append([gox,goy])

    return

N = int(input())

color_list = []
bd_color_list = []


for i in range(N):
    temp = str(input())
    temp1 = []
    temp2 = []
    for j in range(N):
        temp1.append(temp[j])
        if temp[j] == 'R':
            temp2.append('G')
        else:
            temp2.append(temp[j])
    color_list.append(temp1)
    bd_color_list.append(temp2)
block = 0

for i in range(N):
    for j in range(N):
        if color_list[i][j] != 'X':
            tg = color_list[i][j]
            search(i,j,tg)
            block += 1


bd_block = 0

for i in range(N):
    for j in range(N):
        if bd_color_list[i][j] != 'X':
            tg = bd_color_list[i][j]
            bd_search(i,j,tg)
            bd_block += 1

print(block, bd_block)