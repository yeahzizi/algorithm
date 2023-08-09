T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1] * N
    dc = [1, 0, -1, 0] * N

    c, r, d = 0, 0, 0 #초기값 설정

    snail_number = 1

    for x in range(N):  # 이중for문을 돌려야 이차원 배열을 전부 밟을 수 있다.(N*N)
        for y in range(N):
            snail[r][c] = snail_number
            if (c+dc[d] < 0) or (c+dc[d] >= N) or (r+dr[d] < 0) or (r+dr[d] >= N) or (snail[r+dr[d]][c+dc[d]] != 0):
                d = d + 1
            else:
                pass
            r = r + dr[d]
            c = c + dc[d]
            snail_number += 1

    print('#%d'%test_case)
    for p in range(N):
        print(' '.join(list(map(str, snail[p]))))




