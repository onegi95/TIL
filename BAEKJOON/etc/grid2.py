n, m, k = map(int, input().split(' '))

#n 숫자만큼 받는다
num_list = list(map(int, input().split(' ')))

# 만약 제일 큰 수가 2개 이상이면???

if num_list.count(max(num_list)) >= 2:
    print(m*max(num_list))

else:
    new_list = sorted(num_list)
    print(new_list[-2]*(m//(k+1)) + new_list[-1]*(m -( m//(k+1))))