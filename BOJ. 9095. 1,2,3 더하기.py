T = int(input())
for _ in range(T):
    dp = [0] * 12
    n = int(input())
    for i in range(n):
        dp[i] += 1
