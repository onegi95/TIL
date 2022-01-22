import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    char_list = input()
    new_list = []
    count = 0
    num_list = ['1','2','3','4','5','6','7','8','9'] # 숫자 검증용
    for i in range(len(char_list)): # 숫자면 카운트 글자면 아스키 변환 새로운 리스트
        if char_list[i] in num_list:
            count += int(char_list[i])
        else:
            new_list.append(ord(char_list[i]))

    new_list.sort() # 새로운 리스트 정렬해주고

    for i in range(len(new_list)):
        print(chr(new_list[i]),end='') # 다시 문자형태로 출력
    print(count)

