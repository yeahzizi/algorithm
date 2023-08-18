#양 옆에 나보다 높은 건물이 있는지 탐색한다

H, W = map(int, input().split())
block = list(map(int, input().split()))

cnt = 0
for i in range(1, W - 1):
    left = max(block[:i])
    right = max(block[i+1:])

    if min(left, right) > block[i]:
        cnt += min(left, right) - block[i]

print(cnt)
