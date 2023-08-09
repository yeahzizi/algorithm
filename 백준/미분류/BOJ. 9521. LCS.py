one = input()
two = input()

dp = [[0] * (len(two) + 1) for _ in range(len(one) + 1)]

for i in range(1, len(one) + 1):
    for j in range(1, len(two) + 1):
        if one[i - 1] == two[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(one)][len(two)])

