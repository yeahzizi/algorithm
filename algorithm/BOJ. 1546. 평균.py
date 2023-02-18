N = int(input())
num = list(map(int, input().split()))
M = max(num)
ans = 0

for i in range(len(num)):
    ans += num[i]/M*100

print(ans/N)