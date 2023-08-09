def bfs(r, c):
    ans = 1
    Q = [[r, c]]
    while Q:
        [r, c] = Q.pop(0)
        for k in range(4):
            r1 = r + dr[k]
            c1 = c + dc[k]
            if 0 <= r1 < N and 0 <= c1 < N:
                if room[r][c] - room[r1][c1] == -1:
                    Q.append([r1, c1])
                    ans += 1

    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    max_visited = 0
    small_room = 999999

    for i in range(N):
        for j in range(N):
            max_visited = max(max_visited, bfs(i, j))

    for i in range(N):
        for j in range(N):
            if bfs(i, j) == max_visited:
                small_room = min(small_room, room[i][j])

    print(f'#{tc} {small_room} {max_visited}')
