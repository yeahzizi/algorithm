N = int(input())
arr = []

for _ in range(N):
    i, j = map(int, input().split())
    arr.append([i, j])

arr.sort()

for i in arr:
    print(*i)