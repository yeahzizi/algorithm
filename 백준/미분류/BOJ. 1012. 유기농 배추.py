dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for t in range(int(input())):
    M, N, K = map(int, input().split())
    farm = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] += 1
    print(farm)

    ans = 0
    visited = []
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and [i, j] not in visited:
                ans += 1
                visited.append([i, j])
                for dir in range(4):
                    for k in range(1, N):
                        ni, nj = i + dr[dir] * k, j + dc[dir] * k
                        if 0 <= ni < N and 0 <= nj < M:
                            if farm[ni][nj] == 1 and [ni, nj] not in visited:
                                farm[ni][nj] -= 1
                                visited.append([ni, nj])



    print(farm)

    print(ans)
