N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * M for _ in range(N)]

visited[r][c] = 1
ans = 1

while True:
    for dir in range(4):
        d = (d+3) % 4
        rd = r + dx[d]
        cd = c + dy[d]
        if 0 <= rd < N and 0 <= cd < M and room[rd][cd] == 0:
            if visited[rd][cd] == 0:
                visited[rd][cd] = 1
                ans += 1
                r, c = rd, cd
                break


    else:
        rb = r - dx[d]
        cb = c - dy[d]
        if room[rb][cb] == 1:
            print(ans)
            break
        else:
            r, c = rb, cb



