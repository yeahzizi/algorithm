def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3

    if n >= 4:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007

    return dp[n - 1]