N, D = map(int, input().split())
route = []
for _ in range(N):
    x, y, length = map(int, input().split())
    route.append([x, y, length])

dp = [i for i in range(D+1)]
route.sort()

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)
    for x, y, length in route:
        if y < D + 1:
            if x == i:
                dp[y] = min(dp[y], length + dp[x])


print(dp[D])




