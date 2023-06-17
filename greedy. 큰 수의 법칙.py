# 5 8 3
# 2 4 5 4 6

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]

ans = 0

for i in range(m+1):
    if i == 0:
        ans += 0
    elif i == 1:
        ans += first
    elif i == 2:
        ans += first
    elif i % 3 == 1:
        ans += second
    else:
        ans += first

print(ans)

