N = int(input())
num = list(map(int, input().split()))
ans = 0
result = 0

num.sort()

for i in num:
    ans = i + ans
    result += ans

print(result)