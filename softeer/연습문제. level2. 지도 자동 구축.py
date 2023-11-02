import sys
n = int(input())
dp = [0] * (n+1)
dp[0] = 4

key = 1
temp = 2
for i in range(1, n+1):
  dp[i] = (key+temp) * (key+temp)
  temp = key + temp
  key = key * 2

print(dp[n])