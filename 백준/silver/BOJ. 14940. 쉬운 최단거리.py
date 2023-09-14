from collections import deque
def bfs(x, y, length):
    q = deque()
    q.append((x, y, length))
    check[x][y] = 0

    while q:
        x, y, length = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 0 and check[nx][ny] == -1:
                new_length = length + 1
                check[nx][ny] = new_length
                q.append((nx, ny, new_length))


    return check



N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

check = [[-1] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

sx, sy = 0, 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2 and check[i][j] == -1:
            bfs(i, j, 0)


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            print(0, end=" ")
        else:
            print(check[i][j], end=" ")
    print()