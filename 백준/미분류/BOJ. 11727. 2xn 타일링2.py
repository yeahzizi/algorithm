N = int(input())
dp = [0 for i in range(N+1)]

if N == 1:
    print(1)

if N == 2:
    print(3)

if N >= 3:
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N+1):
        dp[i] = dp[i-2] * 2 + dp[i-1]

    print(dp[N] % 10007)