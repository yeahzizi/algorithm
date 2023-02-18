T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [[0] * N for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    r, c = 0, -1
    snail = 1
    dir = 0

    while snail <= N * N:
        r, c = r + dr[dir], c + dc[dir]
        if 0 <= r < N and 0 <= c < N and area[r][c] == 0:
            area[r][c] = snail
            snail += 1
        else:
            r, c = r - dr[dir], c - dc[dir]
            dir = (dir + 1) % 4

    print(f'#{tc}')
    for i in range(N):
        print(*area[i])



