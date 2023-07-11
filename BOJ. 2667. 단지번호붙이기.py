from collections import deque

def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and map[nx][ny] == "1" and visited[nx][ny] == 0:
                map[nx][ny] = "2"
                queue.append((nx, ny))
                cnt += 1

    count.append(cnt)


N = int(input())

map = []
for i in range(N):
    map.append(list(input()))

visited = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and map[i][j] == '1':
            bfs(i, j)
            break

count.sort()
print(len(count))
for i in count:
    print(i)