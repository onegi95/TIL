import sys
sys.stdin = open('input.txt')

N,M = map(int, sys.stdin.readline().split()) # 인원, 파티

R_input = list(map(int, sys.stdin.readline().split()))
if len(R_input) == 1:
    R_list = [0]

else:
    R_list = R_input[1:]

anw = 0
party_list = []
# 진실을 아는 사람이 아무도 없다
if R_list[0] == 0:
    print(M)


# 진실을 아는 사람이 있다!
else:
    # 진실을 알지만, 파티에 참여하지 않았을 경우
    for i in range(M):
        temp = list(map(int,sys.stdin.readline().split()))
        party_list.append(temp[1:])
    for m in range(M):
        temp = party_list[m]
        trg = 0
        for j in range(len(temp)):
            # 진실일 알고있는 파티인지?
            if temp[j] in R_list:
                trg = 1
        if trg == 1:
            for j in range(len(temp)):
                # 진실일 알고있는 파티인지?
                if temp[j] not in R_list:
                    R_list.append(temp[j])
    for m in range(M):
        temp = party_list[-m-1]
        trg = 0
        for j in range(len(temp)):
            # 진실일 알고있는 파티인지?
            if temp[j] in R_list:
                trg = 1
        if trg == 1:
            for j in range(len(temp)):
                # 진실일 알고있는 파티인지?
                if temp[j] not in R_list:
                    R_list.append(temp[j])

    for i in range(M):
        trg = 0
        for j in range(len(party_list[i])):
            if party_list[i][j] in R_list:
                trg = 1
                break

        if trg == 0:
            anw += 1
    print(anw)
