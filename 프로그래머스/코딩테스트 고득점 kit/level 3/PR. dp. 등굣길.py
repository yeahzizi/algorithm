def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i, j in puddles:
        dp[j][i] = 1

    dp[0][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007

    return dp[-1][-1]