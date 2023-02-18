T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # +배열
    dr1 = [1, 0, -1, 0]
    dc1 = [0, 1, 0, -1]

    # *배열
    dr2 = [1, 1, -1, -1]
    dc2 = [1, -1, -1, 1]

    # +배열
    for r in range(N):
        for c in range(N):
            kill = arr[r][c]
            for dir in range(4):
                for i in range(1, M):
                    nr, nc = r + dr1[dir] * i, c + dc1[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)


    for r in range(N):
        for c in range(N):
            kill = arr[r][c]
            for dir in range(4):
                for i in range(1, M):
                    nr, nc = r + dr2[dir] * i, c + dc2[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        kill += arr[nr][nc]
            ans = max(ans, kill)

    print(f'#{tc} {ans}')
