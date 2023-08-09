def perm(depth, acc):
    global answer #함수 아래에서 입력 받을 값을 글로벌로 가져옴

    if acc >= answer:
        return
    if depth == N: #최고 뎁스에 도달하면,
        if answer > acc:
            answer = acc
        return

    for i in range(N):
        if not check[i]:  # 각 기회 안에서 check를 보고 멈출 수 있는지 보고?
            check[i] = 1  # 멈출 수 있다면 if 통과했으니까 자리 차지했다고 표시하고
            sel[depth] = matrix[i]  # 화살표가 떨어진 위치의 재료리스트
            perm(depth+1, acc + matrix[depth][i])
            check[i] = 0  # 돌아나오면서 다시 다음을 위해 초기화!! (중요)
    return answer

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    sel = [0] * N
    answer = 99999999
    perm(0, 0)

    print(f'#{tc} {perm(0, 0)}')

"""
#돌면서 내려 가는 것은 순열 코드와 같은데
#내려갈 때 플러스 해서 가져감
#셋으로 감싸면 아이디 값이 분리됨 > 순열에서 그 충에서 쓸 수 있는 visited로 변모
#셋으로 감싸지 않을거면 remove를 해줘야함
#idx_set = set(idx_set) 이런식
#교수님코드

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = 9999999
    check = [0] * N

    def perm(depth, acc):
        global answer

        if acc >= answer:
            return
        if depth == N:
            if answer > acc:
                answer = acc
            return

        for i in range(N):
            if not check[i]:

"""