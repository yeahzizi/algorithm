# 행, 열 구분 잘하기...

# 효율성  테스트
# 테스트 1 〉	통과 (15.94ms, 10.5MB)
# 테스트 2 〉	통과 (4.38ms, 10.4MB)
# 테스트 3 〉	통과 (10.70ms, 10.3MB)
# 테스트 4 〉	통과 (7.28ms, 10.1MB)

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


#version 2
# m, n 을 정해주니깐 더 빨라짐!
# 효율성  테스트
# 테스트 1 〉	통과 (12.89ms, 10.4MB)
# 테스트 2 〉	통과 (3.39ms, 10.3MB)
# 테스트 3 〉	통과 (8.36ms, 10.4MB)
# 테스트 4 〉	통과 (6.53ms, 10.3MB)

from collections import deque


def solution(maps):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    n = len(maps)  # 세로
    m = len(maps[0])  # 가로

    check = [[-1] * m for _ in range(n)]
    check[0][0] = 1
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and check[nx][ny] == -1 and maps[nx][ny] == 1:
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny))

    return check[n - 1][m - 1]