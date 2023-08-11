M = int(input())
N = int(input())

ans = 0
num = []
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        ans += 1
        num.append(i)

if ans == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))