N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

sell, love = map(int, input().split())

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

time = graph[1][love] + graph[love][sell]

if time >= INF:
    print(-1)
else:
    print(time)