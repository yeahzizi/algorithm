T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range (N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    attack = 0

    for r in range(N):
        for c in range(N):
            if area[r][c] == 2:
                for dir in range(4):
                    for i in range(N):
                        nr, nc = r + dr[dir] * i, c + dc[dir] * i
                        if 0 <= nr < N and 0 <= nc < N and area[nr][nc] <= 0:
                            area[nr][nc] -= 1
                        elif 0 <= nr < N and 0 <= nc < N and area[nr][nc] == 1:
                            break

    for i in range(N):
        for j in range(N):
            if area[i][j] == 0:
                attack += 1
    print(f'#{tc} {attack}')



