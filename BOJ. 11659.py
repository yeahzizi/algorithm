N, M = map(int, input().split())
num = list(map(int, input().split()))

for m in range(M):
    i, j = map(int, input().split())
    ans = 0
    for k in range(i-1, j):
        ans += num[k]
    print(ans)