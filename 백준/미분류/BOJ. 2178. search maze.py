from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue

            if maze[nx][ny] == "0":
                continue

            if maze[nx][ny] == "1":
                maze[nx][ny] = int(maze[x][y]) + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]

print(bfs(0, 0))
