N = int(input())
num = list(map(int, input().split()))

ans = 0
for i in num:
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        ans += 1

print(ans)
