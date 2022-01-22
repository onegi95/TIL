import math
# 문자열로 받아옴
n = input()

# for 로 반복을 해보자
num = 0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        pass
    else:
        num += 1

print(math.ceil(num/2))
