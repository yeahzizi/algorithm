def dfs():
    answer = 0
    for k in range(16):
        for j in range(16):
            if maze[k][j] == 2:
                r, c = k, j

    Q = [[r, c]]
    visited = []
    while Q:
        [r, c] = Q.pop()
        visited.append([r, c])
        for j in range(4):
            r1 = r + dr[j]
            c1 = c + dc[j]
            if 0 <= r1 < 16 and 0 <= c1 < 16:
                if maze[r1][c1] == 0 and [r1, c1] not in visited:
                    Q.append([r1, c1])
                if maze[r1][c1] == 3:
                    answer = 1
                    break

    return answer


for i in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    print(f'#{tc} {dfs()}')