from collections import deque


def solution(n, edge):
    answer = 0
    q = deque()
    arr = [[] for _ in range(n + 1)]
    visited = set()

    for i, j in edge:
        arr[i].append(j)
        arr[j].append(i)

    q.append(1)
    visited.add(1)
    while q:
        size = len(q)
        for _ in range(size):
            now = q.popleft()
            for next_node in arr[now]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)

        answer = size

    return answer