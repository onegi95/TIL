import sys
sys.stdin = open('input.txt')

N = int(input())

tri_list = []

for i in range(N):
    tri_list.append(list(map(int, input().split())))

if N == 1:
    print(tri_list[0][0])
else:
    tri_list[1][0] = tri_list[1][0] + tri_list[0][0]
    tri_list[1][1] = tri_list[1][1] + tri_list[0][0]

    for i in range(2, len(tri_list)):
        tri_list[i][0] = tri_list[i-1][0] + tri_list[i][0]
        tri_list[i][-1] = tri_list[i - 1][-1] + tri_list[i][-1]

        for j in range(1,len(tri_list[i])-1):
            tri_list[i][j] = tri_list[i][j] + max(tri_list[i-1][j-1], tri_list[i-1][j])


    print(max(tri_list[-1]))