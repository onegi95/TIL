import sys
sys.stdin = open('input.txt')

def see_contain(contained):
    q = computer_line[contained]
    anw = 0
    while q:
        temp = q.pop(0)
        if dp_line[temp] == 0:
            q = q+ computer_line[temp]
            dp_line[temp] = 1
            anw += 1
    return anw

computer = int(input())

line = int(input())
dp_line = [0 for _ in range(computer+1)]
dp_line[1] = 1

computer_line = [[] for _ in range(computer+1)]

for _ in range(line):
    N, M = map(int, input().split())
    computer_line[N].append(M)
    computer_line[M].append(N)

print(see_contain(1))

