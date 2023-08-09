T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5000
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A-1, B):
            cnt[i] += 1
    P = int(input())
    C_list = [int(input()) for _ in range(P)]
    result = []

    for i in C_list:
        result.append(cnt[i-1])

    print(f'#{tc}', *result)




