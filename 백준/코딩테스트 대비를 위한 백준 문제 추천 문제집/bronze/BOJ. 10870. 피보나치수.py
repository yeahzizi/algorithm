N = int(input())
dp = [0] * (N+3)
dp[1] = 0
dp[2] = 1

if N >= 2:
    for i in range(3, N+2):
        dp[i] = dp[i-1] + dp[i-2]


print(dp[N+1])