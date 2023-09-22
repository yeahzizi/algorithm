def dfs(x, i): #현재 좌표, 시작 좌표
    global ans
    visited[x] = True
    num = arr[x]
    if not visited[num]:
        dfs(num, i)
    elif visited[num] and num == i:
        ans.append(num)


N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
ans = []

for i in range(1, N+1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)