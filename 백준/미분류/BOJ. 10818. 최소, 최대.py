N = int(input())
num = list(map(int, input().split()))
min_num = 99999999999
max_num = -9999999999

for i in num:
    if i <= min_num:
        min_num = i
    if i >= max_num:
        max_num = i

print(min_num, max_num)