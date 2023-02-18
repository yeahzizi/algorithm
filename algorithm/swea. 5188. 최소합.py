T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]
    dp[0][0] = area[0][0]

    for r in range(N):
        for c in range(N):
            if r == 0:
                dp[r][c] = area[r][c] + dp[r][c-1]
            elif c == 0:
                dp[r][c] = area[r][c] + dp[r-1][c]
            else:
                dp[r][c] = area[r][c] + min(dp[r][c-1], dp[r-1][c])

    print(f'#{tc} {dp[N-1][N-1]}')


