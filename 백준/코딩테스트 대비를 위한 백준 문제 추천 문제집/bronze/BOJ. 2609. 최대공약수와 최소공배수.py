# n, m 둘 중의 작은 수 하나가,
# 최대공약수가 될 수 있다는 사실을 잊지말기

n, m = map(int, input().split())

divide = []
for i in range(1, min(n, m) + 1):
    if n % i == 0 and m % i == 0:
        divide.append(i)

multiple = 0
max_divide = max(divide)
multiple += (n // max_divide) * (m // max_divide) * max_divide

print(max_divide)
print(multiple)