import sys
sys.setrecursionlimit(10**5)

for t in range(int(input())):
    m, n, k = map(int, input().split())
    veg = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        veg[y][x] += 1

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    def dfs(x, y):
        veg[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and veg[nx][ny] == 1:
                veg[nx][ny] = 0
                dfs(nx, ny)

    ans = 0
    for i in range(n):
        for j in range(m):
            if veg[i][j] == 1:
                ans += 1
                dfs(i, j)

    print(ans)
