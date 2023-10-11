def solution(n, costs):
    answer = 0
    visited = [[0] * n for _ in range(n)]

    costs = sorted(costs, key=lambda x: x[2])
    visited = set([costs[0][0]])  # 여기가 되게 중요..시작부분을 꼭 넣어줘야 한다

    while len(visited) != n:
        for i, j, cost in costs:
            if i in visited and j in visited:
                continue
            if i in visited or j in visited:
                visited.update([i, j])
                answer += cost
                break

    return answer