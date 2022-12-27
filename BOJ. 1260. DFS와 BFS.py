N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    n, m = map(int, input().split())
    graph[n][m] += 1
    graph[m][n] += 1

dfs_visited = [0] * (N+1)

def dfs(V):
    dfs_visited[V] = 1
    print(V, end=' ')
    for i in range(N+1):
        if dfs_visited[i] == 0 and graph[i][V]:
            dfs(i)

dfs(V)

from collections import deque

bfs_visited = [0] * (N+1)
def bfs(V):
    bfs_visited[V] = 1
    queue = deque()
    queue.append(V)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(N+1):
            if bfs_visited[i] == 0 and graph[i][node]:
                queue.append(i)
                bfs_visited[i] = 1


print()
bfs(V)




