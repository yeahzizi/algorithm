N, M = map(int, input().split())
r, c, d = map(int, input().split())

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[r][c] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn = 0
while True:
    array[r][c] = 1
    turn_left()
    nr = r + dx[d]
    nc = c + dy[d]

    if array[nr][nc] == 0 and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        cnt += 1
        r = nr
        c = nc
        turn = 0
        continue

    else:
        turn += 1

    if turn == 4:
        nr = r - dx[d]
        nc = c - dy[d]
        if visited[nr][nc] == 0:
            r = nr
            c = nc
        else:
            break
        turn = 0

print(cnt)





