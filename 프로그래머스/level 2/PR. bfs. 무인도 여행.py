import sys

sys.setrecursionlimit(10 ** 5)


def check(x, y, maps, arr, n, m, cnt):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and maps[nx][ny] != "X":
            arr[nx][ny] += 1
            cnt += int(maps[nx][ny])
            cnt = check(nx, ny, maps, arr, n, m, cnt)

    return cnt


def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])
    arr = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and arr[i][j] == 0:
                arr[i][j] = 1
                answer.append(check(i, j, maps, arr, n, m, int(maps[i][j])))

    if not answer:
        return [-1]
    else:
        answer.sort()
        return answer
