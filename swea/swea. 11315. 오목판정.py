T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = [input() for _ in range(N)]
    space_zip = list(map(list, zip(*space)))
    YnN = 0

    for i in range(N):
        for j in range(N-5+1):
            if space[i][j:j+5] == "ooooo":
                YnN += 1
            if "".join(space_zip[i][j:j+5]) == "ooooo":
                YnN += 1

    for i in range(N-5+1):
        for j in range(N-5+1):
            if space[i][j] == "o" and space[i + 1][j+1] == "o" and space[i + 2][j + 2] == "o" and space[i + 3][j + 3] == "o" and space[i + 4][j + 4] == "o":
                YnN += 1
            if space[i][j + 4] == "o" and space[i + 1][j + 3] == "o" and space[i + 2][j + 2] == "o" and space[i + 3][j + 1] == "o" and space[i + 4][j] == "o":
                YnN += 1

    if YnN > 0:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')