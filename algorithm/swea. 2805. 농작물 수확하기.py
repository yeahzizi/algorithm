for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    farm_count = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if j == N//2 and i <= N//2:
                farm_count[i][j-i:j+i+1] = farm[i][j-i:j+i+1]

            elif j == N//2 and i > N//2:
                farm_count[i][abs(j-i):abs(j-i+N)] = farm[i][abs(j-i):abs(j-i+N)]

    farm_sum = 0
    for i in range(N):
        for j in range(N):
            farm_sum += farm_count[i][j]

    print(f'#{tc+1} {farm_sum}')








