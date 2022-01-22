import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    def solution(p):
        char = p
        new_char = ''
        status = 0
        i = 0
        while i < len(char) - 1:
            i += 1
            if char[i] == "(":
                status += 1
            elif char[i] == ")":
                status -= 1
            else:
                continue

            if status < 0:
                start = i
                while status < 0:
                    i += 1
                    if char[i] == "(":
                        status += 1
                    elif char[i] == ")":
                        status -= 1
                end = i
                half = (end - start + 1) // 2
                new_char = new_char + "(" * half + ")" * half
            else:
                new_char = new_char + char[i]

        return new_char

    p = input()
    print(solution(p))