S = int(input())

ans = 0
cnt = 0
for i in range(1, S+1):
    ans += i
    cnt += 1
    if ans > S:
        cnt -= 1
        break

print(cnt)