for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    ans = "possible"

    for r in range(N):
        for c in range(M):
            if arr[r][c] == ".":
                for dir in range(4):
                    nr, nc = r + dr[dir], c + dc[dir]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == "?":
                            arr[nr][nc] = "#"

            if arr[r][c] == "#":
                for dir in range(4):
                    nr, nc = r + dr[dir], c + dc[dir]
                    if 0 <= nr < N and 0 <= nc < M:
                        if arr[nr][nc] == "?":
                            arr[nr][nc] = "."

    for r in range(N):
        for c in range(M):
            for dir in range(4):
                nr, nc = r + dr[dir], c + dc[dir]
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != "?":
                    if arr[r][c] == arr[nr][nc]:
                        ans = "impossible"
                        break

    print(f'#{tc} {ans}')




