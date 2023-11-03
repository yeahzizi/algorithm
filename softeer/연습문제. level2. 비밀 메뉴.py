# 문제 설명 진짜 불친절..

import sys
m, n, k = map(int, input().split())
secret = list(map(int, input().split()))
user = list(map(int, input().split()))

if m <= n:
  for i in range(n):
    if user[i:i+m] == secret:
      print("secret")
      break
  else:
    print("normal")
else:
  print("normal")