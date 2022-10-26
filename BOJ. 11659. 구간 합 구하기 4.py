import sys
input = sys.stdin.readline

N, M = map(int, input().split()) 
num = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        num[i] = num[i]
    if i >= 1:
        num[i] = num[i] + num[i-1]

for m in range(M):
    i, j = map(int, input().split())
    ans = 0
    if i == 1:
        ans = num[j-1]
    elif i >= 2:
        ans = num[j-1] - num[i-2]
    print(ans)


