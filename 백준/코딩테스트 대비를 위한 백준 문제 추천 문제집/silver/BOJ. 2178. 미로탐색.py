from collections import deque

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(input()))

check = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    queue = deque()
    queue.append([x, y])
    check[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == 0 and maze[nx][ny] == "1":
                queue.append([nx, ny])
                check[nx][ny] = check[x][y] + 1

    return check[N-1][M-1]

print(dfs(0, 0))