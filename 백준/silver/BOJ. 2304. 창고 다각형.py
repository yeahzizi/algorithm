N = int(input())
arr = []
for _ in range(N):
    L, H = map(int, input().split())
    arr.append([L, H])

arr1 = sorted(arr, key=lambda x: x[1])
tall = arr1[-1]


arr.sort()
ans = 0
x, y = arr[0][0], arr[0][1]
for i, j in arr:
    if i == tall[0] and j == tall[1]:
        ans += (i - x) * y
        break
    else:
        if y < j:
            ans += (i-x) * y
            x = i
            y = j

x, y = arr[-1][0], arr[-1][1]
arr.pop()
for value in reversed(range(len(arr))):
    i, j = arr[value][0], arr[value][1]
    if i == tall[0] and j == tall[1]:
        ans += (x - i) * y
        break
    else:
        if y < j:
            ans += (x - i) * y
            x = i
            y = j

print(ans + tall[1])
