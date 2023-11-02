# int 오버플로우에 주의해야 한다
# 파이썬은 1초에 1억번 연산

k, p, n = map(int, input().split(" "))

for i in range(n):
    k = k * p
    k = k % 1000000007

print(k % 1000000007)