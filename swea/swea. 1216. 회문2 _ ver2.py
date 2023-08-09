for tc in range(10):
    T = int(input())
    pal = [input() for _ in range(100)]
    pal_zip = list(map(list, zip(*pal))) #2차원 배열 zip 만들기
    max_pal = 0

    for i in range(100):
        for j in range(101):
            for r in range(101):
                if pal[i][j:r] == pal[i][j:r][::-1]:
                    if max_pal <= len(pal[i][j:r]):
                        max_pal = len(pal[i][j:r])
                if pal_zip[i][j:r] == pal_zip[i][j:r][::-1]:
                    if max_pal <= len(pal_zip[i][j:r]):
                        max_pal = len(pal_zip[i][j:r])

    print(f'#{tc+1} {max_pal}')