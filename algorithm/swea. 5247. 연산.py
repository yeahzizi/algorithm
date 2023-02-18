from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dp = [0] * 1000001
    deq = deque([N])

    while deq:
        ans = deq.popleft()
        if ans == M:
            break
        for i in [ans + 1, ans - 1, ans * 2, ans - 10]:
            if 0 < i <= 1000000 and dp[i] == 0:
                dp[i] = dp[ans] + 1
                deq.append(i)

    print(f'#{tc} {dp[M]}')








