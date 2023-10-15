from collections import deque


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    x, y = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                x, y = i, j
            elif maps[i][j] == "L":
                lx, ly = i, j
            elif maps[i][j] == "E":
                ex, ey = i, j

    goal = [[lx, ly], [ex, ey]]

    for i in range(2):
        gx, gy = goal[i]
        q = deque()
        q.append((x, y, 0))
        check = [[0] * m for _ in range(n)]
        check[x][y] = 1

        while q:
            x, y, level = q.popleft()

            if x == gx and y == gy:
                answer += level
                break

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and check[nx][ny] == 0:
                    q.append((nx, ny, level + 1))
                    check[nx][ny] = 1

        else:
            answer = 0

        if answer == 0:
            break
        x, y = lx, ly

    if answer == 0:
        return -1
    else:
        return answer

