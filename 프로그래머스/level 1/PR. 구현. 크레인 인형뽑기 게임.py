def solution(board, moves):
    answer = 0
    cnt = []
    n = len(moves)
    m = len(board)

    for i in range(n):
        for j in range(m):
            if board[j][moves[i] - 1] != 0:
                cnt.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

        if len(cnt) > 1:
            if cnt[-1] == cnt[-2]:
                answer += 2
                cnt.pop()
                cnt.pop()

    return answer