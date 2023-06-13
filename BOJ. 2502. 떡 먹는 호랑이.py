<<<<<<< HEAD
#피보나치 수열
d, k = map(int, input().split())

#fibo(d-1)*a + fibo(d)*b
#K = ax + by

x = 1
y = 0
for i in range(d-1):
    x, y = y, x+y
for a in range(1, 100000):
    if (k - (x*a)) % y == 0:
        print(a, (k - (x*a))//y, sep="\n") #출력 시 값 사이에 문자를 넣기
        break
=======
d, k = map(int, input().split())
dp = [0] * (d+1)

for i in range(3, d+1):
    A = dp[0]
    B = dp[1]
    dp[2] = A + B
    dp[i] = dp[i-1] + dp[i-2]

print(dp)
>>>>>>> 9b8c98dfe6f63dceebd42034028af437472daa71
