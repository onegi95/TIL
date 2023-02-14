import sys
sys.stdin = open('input.txt')

def diffusion(x,y,a):
    move_x = [0,0,-1,1]
    move_y = [-1,1,0,0]
    



def air_condition():
    pass


T = int(input())

for tc in range(T):
    R, C, T = map(int, input().split())
    air_map = []
    for _ in range(R):
        air_map.append(list(map(int, input().split())))

#     공기 청정기 위치 확인

#   공기 청정기로 인한 순환 확인

#  확산도 확인을 해야 되는데.... 그렇다고 bf로 모두 체크하자니 일이 너무 많다

#  그럼 dp 맵을 하나 만들어서, 좌표 + 먼지 이동량 으로 계산하는 건 어떨까? =>

# 이동량을 계산한 다음 => 다시 적용시켜 주는 것


