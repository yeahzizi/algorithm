T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result1 = []
    result2 = []

    for k in range(N - K+1):
        for s in range(N - K+1):
            ans1 = 0
            for i in range(k, k+K):
                for j in range(s, s+K):
                    ans1 += arr[i][j]
                    cnt += 1
                    if cnt == K * K:
                        result1.append(ans1)
                        cnt = 0

    for k in range(N - K + 1):
        for s in range(N - K + 1):
            ans2 = 0
            for i in range(k+1, k + K-1):
                for j in range(s+1, s + K-1):
                    ans2 += arr[i][j]
                    cnt += 1
                    if cnt == (K-2) * (K-2):
                        result2.append(ans2)
                        cnt = 0

    final = 0
    for i in range(len(result1)):
        if result1[i] - result2[i] >= final:
            final = result1[i] - result2[i]

    print(f'#{tc} {final}')