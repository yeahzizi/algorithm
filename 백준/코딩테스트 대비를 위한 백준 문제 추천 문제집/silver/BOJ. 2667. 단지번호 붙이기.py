from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    global cnt
    cnt = 0

    while q:
        nx, ny = q.popleft()
        for d in range(4):
            ni = nx + dx[d]
            nj = ny + dy[d]
            if 0 <= ni < N and 0 <= nj < N and maps[ni][nj] == "1":
                q.append((ni, nj))
                maps[ni][nj] = "-1"
                cnt += 1

    return cnt


N = int(input())
maps = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []


for i in range(N):
    for j in range(N):
        if maps[i][j] == "1":
            result = bfs(i, j)
            maps[i][j] = "-1"
            if result == 0:
                ans.append(1)
            else:
                ans.append(result)

print(len(ans))
ans.sort()
for i in ans:
    print(i)




