# BFS로 destination에서 출발하여 갈 수 있는 모든 노드를 검사
from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    queue = deque([destination])
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    visited[destination] = 0
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                queue.append(node)

    return [visited[i] for i in sources]