import sys


def check(x, y):
    global cnt
    cnt += 1
    new[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if new[nx][ny] == 0 and arr[nx][ny] == 1:
                new[nx][ny] = 1
                check(nx, ny)


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

new = [[0] * n for _ in range(n)]

ans = []
for i in range(n):
    for j in range(n):
        if new[i][j] == 0 and arr[i][j] == 1:
            cnt = 0
            check(i, j)
            ans.append(cnt)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
