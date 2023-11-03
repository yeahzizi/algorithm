import sys

n, m = map(int, input().split())

dp = [0] * 101
now = 0
for _ in range(n):
  a, b = map(int, input().split())
  for k in range(now+1, now+a+1):
    dp[k] = b
  now = now + a

check = [0] * 101
now = 0
for _ in range(m):
  a, b = map(int, input().split())
  for k in range(now+1, now+a+1):
    check[k] = b
  now = now + a


ans = 0
for i in range(101):
  ans = max(check[i] - dp[i], ans)

print(ans)