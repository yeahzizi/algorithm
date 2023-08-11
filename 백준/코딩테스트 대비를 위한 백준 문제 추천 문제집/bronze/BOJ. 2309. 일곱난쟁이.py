# 뭔지 모르겠지만 어려워...

num = []
for _ in range(9):
    num.append(int(input()))

one, two = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(num) - num[i] - num[j] == 100:
            one = num[i]
            two = num[j]

num.remove(one)
num.remove(two)
num.sort()

for i in num:
    print(i)