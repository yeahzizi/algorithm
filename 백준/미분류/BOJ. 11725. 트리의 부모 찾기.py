import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
for _ in range(N - 1):
    n, m = map(int, sys.stdin.readline().split())
    tree[n].append(m)
    tree[m].append(n)

visited = [False] * (N+1)
parent = [0 for _ in range(N+1)]

def dfs(node):
    visited[node] = True
    for i in tree[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)
    return

dfs(1)
for i in range(2, len(parent)):
    print(parent[i])

