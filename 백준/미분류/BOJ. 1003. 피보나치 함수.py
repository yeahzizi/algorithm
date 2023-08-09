T = int(input())
for i in range(T):
    num = int(input())
    dp = [0] * (num + 2)

    if num == 0: #피보나치 함수가 f(0)일때
        dp[0] = 0
        dp[1] = 1 #피보나치 함수가 f(1)일 때도 값을 주어야 1의 개수를 구할 수 있다.

    elif num == 1: #피보나치 함수가 f(1)일때
        dp[0] = 0
        dp[1] = 1

    elif num == 2: #피보나치 함수가 f(2)일때
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

    elif num >= 3: #피보나치 함수가 f(3) 이상일 때
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for j in range(3, num+1):
            dp[j] = dp[j-1] + dp[j-2] #전 값과 전전 값을 더하면 구하고자 하는 값이 나온다.

    print(dp[num-1], dp[num])

