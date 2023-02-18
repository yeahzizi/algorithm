T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    bomb = [list(map(int, input().split())) for _ in range(M)]

    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    kill = 0
    ans = 0

    visited = []


    for i in range(M):
        kill = area[bomb[i][0]][bomb[i][1]]
        for r in range(N):
            for c in range(N):
                kill_sum = 0
                for dir in range(4):
                    for j in range(0, bomb[i][2]+1):
                        nr, nc = bomb[i][0] + dr[dir] * j, bomb[i][1] + dc[dir] * j
                        if 0 <= nr < N and 0 <= nc < N and [nr, nc] not in visited:
                            visited.append([nr, nc])
                            kill_sum += area[nr][nc]

                ans += kill_sum
    print(f'#{tc} {ans}')







