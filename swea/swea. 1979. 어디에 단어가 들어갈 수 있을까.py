T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    zipped_puzzle = [[] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            zipped_puzzle[i] += [puzzle[j][i]]
    # print(zipped_puzzle)
    # print(puzzle, zipped_puzzle)

    new_puzzle = [[0] * (N + 2) for _ in range(N + 2)]
    for a in range(1, N+1):
        for b in range(1, N+1):
            new_puzzle[a][b] = puzzle[a-1][b-1]
    print(new_puzzle)

    new_zipped_puzzle = [[0] * (N + 2) for _ in range(N + 2)]
    for c in range(1, N + 1):
        for d in range(1, N + 1):
            new_zipped_puzzle[c][d] = zipped_puzzle[c - 1][d - 1]

    count = 0
    for e in range(N + 2):
        for f in range(N - K + 1):
            if new_puzzle[e][f] == 0 and new_puzzle[e][f + 1 + K] == 0:
                if 0 not in new_puzzle[e][f +1: f + K + 1]:
                    count += 1
            if new_zipped_puzzle[e][f] == 0 and new_zipped_puzzle[e][f + 1 + K]==0:
                if 0 not in new_zipped_puzzle[e][f +1: f + K + 1]:
                    count += 1



    print(f'#{test_case} {count}')







