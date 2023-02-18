for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    ans = 'NO'

    dr = [1, 0, -1, 0, 1, 1, -1, -1]
    dc = [0, 1, 0, -1, 1, -1, -1, 1]

    for r in range(N):
        for c in range(N):
            for dir in range(8):
                cnt = 0
                for k in range(5):
                    nr, nc = r + (dr[dir] * k), c + (dc[dir] * k)
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] == 'o':
                            cnt += 1

                if cnt == 5:
                    ans = 'YES'
                    break

    print(f'#{tc} {ans}')


