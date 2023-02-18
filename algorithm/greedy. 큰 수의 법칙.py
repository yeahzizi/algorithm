n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n-1]
second = num[n-2]

count = m // (k+1) * k
print(count)

count += m % (k+1)
print(count)

result = 0
result += (count) * first
result += (m - count) * second

print(result)