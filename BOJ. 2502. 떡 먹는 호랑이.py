d, k = map(int, input().split())
dp = [0] * (d+1)

for i in range(3, d+1):
    A = dp[0]
    B = dp[1]
    dp[2] = A + B
    dp[i] = dp[i-1] + dp[i-2]

print(dp)