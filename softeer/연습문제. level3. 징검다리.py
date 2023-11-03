import sys

input = sys.stdin.readline
n = int(input())
bridge = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    cnt = 0
    for j in range(i):
        if bridge[j] < bridge[i]:
            cnt = max(cnt, dp[j])

    dp[i] = cnt + 1

print(max(dp))
