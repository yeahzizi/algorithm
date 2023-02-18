#델타검색으로 풀자
#사방탐색으로 검사했을 때 O가 있으면 no, O의 개수가 8개가 아니어도 no
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input())+1):
    chess = [list(input()) for _ in range(8)]
    ans = 'yes'
    cnt = 0

    for r in range(8):
        for c in range(8):
            if chess[r][c] == "O":
                cnt += 1
                for dir in range(4):
                    for i in range(1, 8):
                        nr, nc = r + dr[dir] * i, c + dc[dir] * i
                        if 0 <= nr < 8 and 0 <= nc < 8:
                            if chess[nr][nc] == "O":
                                ans = 'no'

    if cnt != 8:
        ans = 'no'

    print(f'#{tc} {ans}')
