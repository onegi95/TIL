import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split()) #N = 볼링공 갯수, M = 최대 무게

    ball_list = list(map(int, input().split()))

    #각각의 볼의 숫자를 새어 저장한다
    weight_list = [0]*(M+1)
    for wg in range(M+1):
        weight_list[wg] += ball_list.count(wg)

    # 2개를 고르는 경우의 수를 모두 count 에 더해준다
    count = 0
    for cal in range(1,len(weight_list)):
        for cal2 in range(cal+1,len(weight_list)):
            count += weight_list[cal]*weight_list[cal2]
        
    print(count)