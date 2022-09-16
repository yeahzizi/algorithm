T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tri = [[1] * (i+1) for i in range(N)] #1이 채워져 있는 삼각형을 받는다.

    for i in range(N):
        for j in range(len(tri[i])-1):  #이차원 배열의 길이가 1, 2, 3, 4개 이고, 길이가 3 이상부터 덧셈을 해야함
            if i >= 2 and j >= 1:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{tc}')
    for i in tri:
        print(*i)
