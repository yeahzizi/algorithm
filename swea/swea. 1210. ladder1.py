dx = [-1, 0, -1]
dy = [0, -1, 0]

#당첨에서 올라갈 거임
x, y = 0, 0
d = 0
start = 99

T = int(input())
for tc in range(1, T+1):
    space = [list(map(int, input().split())) for _ in range(100)]

    for i in range(99, -1, -1):
        if space[start][i] == 2:
            x, y = start, i  # 당첨이자 시작점
            break

    while True:
        if x == 0:
            break
        if space[x][y-1]:
            d = 1
            while True:
                x += dx[d]
                y += dy[d]
                if not space[x][y - 1]:
                    break  #
                elif space[x][y + 1]:
                    d = 2
                    while True:
                        x += dx[d]
                        y += dy[d]
                        if not space[x][y + 1]:
                            break
                d = 0
                x += dx[d]
                y += dy[d]
            print(f'#{tc + 1} {y - 1}')





