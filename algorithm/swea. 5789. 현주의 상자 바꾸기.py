T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    cnt = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())

        for i in range(L-1, R):
            cnt[i] = q

    print(f'#{tc}', *cnt)
