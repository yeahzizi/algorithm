T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]
    small_square = [list(map(int, input().split())) for _ in range(M)]
    empty = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            for k in range(M):
                for s in range(small_square[k][2]):
                    for m in range(small_square[k][2]):
                        i, j = small_square[k][0] + s, small_square[k][1] + m
                        if 0 <= i < N and 0 <= j < N:
                            empty[i][j] = square[i][j]

    for i in range(N):
        for j in range(N):
            ans += empty[i][j]

    print(f'#{tc} {ans}')



