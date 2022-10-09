for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    russia = [list(input()) for _ in range(N)]
    ans = []

    for i in range(1, N-1):
        for j in range(i+1, N):
            blank = [["W"] * M for _ in range(i)] + [["B"] * M for _ in range(i, j)] + [["R"] * M for _ in range(j, N)]
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if russia[r][c] != blank[r][c]:
                        cnt += 1
            ans.append(cnt)

    print(f'#{tc} {min(ans)}')
