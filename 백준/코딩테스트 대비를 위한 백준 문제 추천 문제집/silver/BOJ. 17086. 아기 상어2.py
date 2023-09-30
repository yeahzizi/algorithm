from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
ans = 0

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = True
    while q:
        x, y, level = q.popleft()
        if level == max(M, N):
            return 0
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    q.append([nx, ny, level+1])
                    visited[nx][ny] = 1
                else:
                    return level+1


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans = max(ans, bfs(i, j))

print(ans)