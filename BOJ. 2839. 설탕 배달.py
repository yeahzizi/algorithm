N = int(input())
cnt = []
ans = 999999

for i in range(1001):
    for j in range(1334):
        if N == 5 * i + 3 * j:
            cnt.append([i, j])

if not cnt:
    ans = -1

for i, j in cnt:
    if i+j <= ans:
        ans = i+j

print(ans)