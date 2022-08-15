T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    space = [[0] * 10 for _ in range(10)] #arr2 = []
                                          #for i in range(10):
                                         #arr2.append([0]*10)
    for i in range(1, N+1):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        count = 0
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                space[r][c] += color


    for r in range(10):
        for c in range(10):
            if space[r][c] >= 3:
                count += 1

    print(f'#{test_case} {count}')
