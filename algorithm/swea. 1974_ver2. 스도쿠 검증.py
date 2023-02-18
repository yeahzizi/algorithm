T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    cnt1 = [0] * 10
    cnt = 0
    ans = 0


    #세로 확인
    for i in range ( len ( sudoku ) ):
        cnt = 0
        cnt2 = [0] * 10
        for j in range ( len ( sudoku ) ):
            cnt2[sudoku[j][i]] += 1
            cnt += 1
            if cnt == 9:
                if cnt2 == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    ans += 1


    #가로 확인
    for i in range(len(sudoku)):
        cnt = 0
        cnt2 = [0] * 10
        for j in range(len(sudoku)):
            cnt2[sudoku[i][j]] += 1
            cnt += 1
            if cnt == 9:
                if cnt2 == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    ans += 1

    # 3 * 3 확인
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                cnt3 = [0] * 10
                cnt = 0
                for r in range(3):
                    for c in range(3):
                        cnt3[sudoku[i+r][j+c]] += 1
                        cnt += 1
                        if cnt == 9:
                            if cnt3 == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                                ans += 1

    print(ans)
    if ans == 27:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
