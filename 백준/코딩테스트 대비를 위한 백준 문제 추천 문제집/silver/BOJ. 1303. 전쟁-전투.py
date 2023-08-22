from collections import deque

def bfs():
    queue.append((i, j))
    check[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and war[nx][ny] == war[x][y] and check[nx][ny] == 0:
                check[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt

N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]
check = [[0] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
white = 0
blue = 0

for i in range(M):
    for j in range(N):
        if check[i][j] == 0:
            ans = bfs()
            if war[i][j] == "W":
                white += ans ** 2
            else:
                blue += ans ** 2

print(white, blue)