N, K = map(int, input().split())
value = [int(input()) for _ in range(N)]
dp = [1e9] * 100001
dp[0] = 0

for v in value:
    for i in range(v, K+1):
        dp[i] = min(dp[i], dp[i-v]+1)


if dp[K] == 1e9:
    print(-1)
else:
    print(dp[K])

