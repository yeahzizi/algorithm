for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = "yes"
    visited = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                arr[i][j] = 1
                visited.append([i, j])
            elif arr[i][j] == ".":
                arr[i][j] = 0

    max_v = max(visited)
    min_v = min(visited)

    area = 0
    if max_v[0]-min_v[0] != max_v[1]-min_v[1]:
        ans = "no"
    else:
        area = ((max_v[0]-min_v[0])+1) * ((max_v[0]-min_v[0])+1)

    result = 0
    for i in range(min_v[0], max_v[0]+1):
        for j in range(min_v[1], max_v[1]+1):
            result += arr[i][j]

    if result != area:
        ans = "no"

    print(f'#{tc} {ans}')

