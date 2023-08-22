# 행, 열 구분 잘하기...

from collections import deque

def solution(maps):
    check = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    check[0][0] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and check[ny][nx] == -1 and maps[ny][nx] == 1:
                queue.append((ny, nx))
                check[ny][nx] = check[y][x] + 1

    return check[len(maps) - 1][len(maps[0]) - 1]