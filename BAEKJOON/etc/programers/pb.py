def solution(n, lost, reserve):
    anw = n
    set_reserve = list(set(reserve) - set(lost))
    set_lost = list(set(lost) - set(reserve))
    anw -= len(set_lost)
    for j in range(len(set_lost)):
        if set_lost[j]+1 in set_reserve:
            set_reserve.remove(set_lost[j]+1)
            anw += 1
        elif set_lost[j]-1 in set_reserve:
            set_reserve.remove(set_lost[j]-1)
            anw += 1

    return anw

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))