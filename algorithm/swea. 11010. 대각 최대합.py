T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]
    ans = 0

    #대각선
    for r in range(N):
        for c in range(N):
            start = arr[r][c]
            for dir in range(4):
                for i in range(1, N):
                    nr, nc = r + dr[dir] * i, c + dc[dir] * i
                    if 0 <= nr < N and 0 <= nc < N:
                        start += arr[nr][nc]

            ans = max(ans, start)

    print(f'#{tc} {ans}')




