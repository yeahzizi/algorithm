def solution(x, y, n):
    answer = 0
    dp = [-1] * (y + 2)
    dp[x] = 0

    for i in range(x + 1, y + 2):
        if dp[i - n] != -1:
            if dp[i] == -1:
                dp[i] = dp[i - n] + 1
            else:
                dp[i] = min(dp[i - n] + 1, dp[i])
        if i % 2 == 0 and dp[i // 2] != -1:
            if dp[i] == -1:
                dp[i] = dp[i // 2] + 1
            else:
                dp[i] = min(dp[i // 2] + 1, dp[i])
        if i % 3 == 0 and dp[i // 3] != -1:
            if dp[i] == -1:
                dp[i] = dp[i // 3] + 1
            else:
                dp[i] = min(dp[i // 3] + 1, dp[i])

    return dp[y]