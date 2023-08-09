n, m = map(int, input().split())

num = []
for i in range(1, n+1):
    if n % i == 0:
        num.append(i)

if len(num) <= m-1:
    print(0)
else:
    num.sort()
    print(num[m-1])