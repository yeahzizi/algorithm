def dfs():
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                r, c = i, j

    Q = [[r, c]]
    visited = []
    while Q:
        [r, c] = Q.pop()
        visited.append([r, c])
        for i in range(4):
            r1 = r + dr[i]
            c1 = c + dc[i]
            if 0 <= r1 < N and 0 <= c1 < N:
                if not maze[r1][c1] and [r1, c1] not in visited:
                    Q.append([r1, c1])
                if maze[r1][c1] == 2:
                    ans = 1
                    break

    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    print(f'#{tc} {dfs()}')
