S = int(input())

total = 0
cnt = 0
for i in range(1, S+1):
    total = total + i
    cnt += 1
    if total > S:
        cnt -= 1
        break

print(cnt)