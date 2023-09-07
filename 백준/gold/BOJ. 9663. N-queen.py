def back_tracking():
    global ans
    if len(cnt) == N:
        ans += 1
        return
    for i in range(1, N+1):
        for j in range(1, N+1):
            if chess[i][j] != 1:
                for d in range(8):
                    di = i + dx[d]
                    dj = j + dx[d]
                    if di >= 1 and di < N and dj >= 1 and dj < N:
                        if chess[di][dj] == 1:
                            break
                        else:
                            cnt.append(chess[i][j])
                            back_tracking()
                            cnt.pop()



N = int(input())
chess = [[1] * N for _ in range(1)] + [[1] * 1 + [0] * N for _ in range(N)]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
cnt = []
ans = 0
back_tracking()
print(ans)

