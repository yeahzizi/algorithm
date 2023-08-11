A, B = map(int, input().split())

num = []
while len(num) <= 1000:
    for i in range(1, 100):
        num += ([i] * i)
        if len(num) >= 1000:
            break


ans = 0
for i in range(A-1, B):
    ans += num[i]

print(ans)