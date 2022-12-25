T = int(input())
for i in range(T):
    num = int(input())
    dp = [0] * (num + 2)

    if num == 0:
        dp[0] = 0
        dp[1] = 1

    elif num == 1:
        dp[0] = 0
        dp[1] = 1

    elif num == 2:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

    elif num >= 3:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for j in range(3, num+1):
            dp[j] = dp[j-1] + dp[j-2]

    print(dp[num-1], dp[num])

