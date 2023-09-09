N = int(input())
board = [list(input()) for _ in range(N)]
ans = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N-1):
    cnt = 1
    for j in range(N-1):
        if board[i][j] == board[i][j+1] or board[i][j] == board[i+1][j]:
            cnt += 1
        elif board[i][j] != board[i][j+1]:
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < N and 0 <= y < N and board[i][j] == board[x][y]:
                    board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                    cnt += 1
                    break
        elif board[i+1][j] != board[i][j]:
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < N and 0 <= y < N and board[i][j] == board[x][y]:
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                    cnt += 1
                    break

    ans.append(cnt)

print(max(ans))



