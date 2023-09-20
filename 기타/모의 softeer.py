import sys


def dfs(letter, idx, cnt):
    global ans
    num = min(len(alp), idx + 1 + k)
    for i in range(idx + 1, num):
        if alp[i] != letter:
            alp[i] = letter
            cnt = cnt + 1
            ans = ans + 1
            if cnt == k:
                return True
        else:
            cnt = cnt + 1
            if cnt == k:
                return True


n, k = map(int, input().split())
alp = list(input())
ans = 0

start = alp[0]
for i in range(len(alp)):
    if start == alp[i]:
        continue
    else:
        dfs(alp[i], i, 1)
        start = alp[i] # i + k 로 바꿔야함

print(ans)