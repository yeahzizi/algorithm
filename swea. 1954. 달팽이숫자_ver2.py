T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [[0] * N for _ in range(N)]
    visited = []
    snail = 1

    dr = [1, 0, -1, 0] * N
    dc = [0, 1, 0, -1] * N

    for r in range(N):
        for c in range(N):
            area[r][c] += snail
            for i in range(4):
                r, c = r + dr[i], c + dc[i]
            snail += 1

    print(area)



