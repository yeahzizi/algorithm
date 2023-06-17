n, m = map(int, input().split())

ans = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_num = min(data)
    ans = max(ans, min_num)

print(ans)