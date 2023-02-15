n = str(input())

le = len(n)
under = 0

for i in n:
    if i == '_':
        under += 1
print(le + 2+ (under*5))