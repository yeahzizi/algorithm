# 가치의 합이 i가 되는 경우의 수를 구하는 부분 문제
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

dp = [0 for i in range(K+1)]
dp[0] = 1

for i in coin:
    for j in range(i, K+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[K])






