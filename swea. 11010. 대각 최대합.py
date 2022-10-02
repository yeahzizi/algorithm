T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    #대각선
    for r in range(N):
        for c in range(N):
            