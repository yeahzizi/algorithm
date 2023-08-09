def perm(depth):
    global answer

    if depth == N - 1:
        acc = 0
        for i in range(N):
            acc += matrix[sel[i]-1][sel[i+1]-1]
        if answer > acc:
            answer = acc
        return

    for i in range(1, N):
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth+1] = visited[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1)
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    sel = [1] * (N+1)
    visited = list(range(1, N+1))
    answer = 99999999
    perm(0)

    print(f'#{tc} {answer}')