num = []
for _ in range(3):
    num.append(int(input()))
result = str(num[0] * num[1] * num[2])
cnt = [0] * 10

for i in result:
    cnt[int(i)] += 1

for i in cnt:
    print(i)