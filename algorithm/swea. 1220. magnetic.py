for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0

    for i in range(N):
        flag = 0
        for j in range(N):
            if table[j][i] == 1:
                flag = 1
            elif table[j][i] == 2:
                if flag == 1:
                    cnt += 1
                    flag = 0

    print(f'#{tc} {cnt}')


