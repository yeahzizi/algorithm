N = int(input())
T = []
P = []
dp = [0] * (N+1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(P[i] + dp[T[i] + i], dp[i+1])

print(max(dp))
