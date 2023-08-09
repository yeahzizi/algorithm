T = int(input())
for tc in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_zip = list(map(list, zip(*sudoku)))
    cnt = [0] * 10
    ans = 0
    count = 0

    for i in range(9):
        for j in range(9):
            if len(set(sudoku[i])) == 9 and len(set(sudoku_zip[i])) == 9:
                ans += 1
            else:
                ans += 0

    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                for r in range(3):
                    for c in range(3):
                        cnt[sudoku[i+r][j+c]] = 1
                if cnt[1:] == [1, 1, 1, 1, 1, 1, 1, 1, 1]:
                    count += 1

    if ans == 81 and count == 9:
        print(f'#{tc+1}', 1)
    else:
        print(f'#{tc+1}', 0)














"""
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    cnt3 = [0] * 10

    for i in range(3):
        for j in range(3):
            cnt1[sudoku[i][j]] += 1

    for i in range(9):
        cnt2[sudoku[i]] += 1
    print(cnt2)
"""









