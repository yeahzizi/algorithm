T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0] * (N+1)
    ans = 0

    for i in arr:
        cnt[i] += 1

    for i in range(len(cnt)):
        if cnt[i] != 0:
            ans += 1
            if ans == K:
                print(f'#{tc} {i}')

