import sys
N = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))
cnt = {}

for j in arr2:
    cnt[j] = 0

for j in arr2:
    for i in arr1:
        if j == i:
            cnt[j] += 1

print(*cnt.values())
