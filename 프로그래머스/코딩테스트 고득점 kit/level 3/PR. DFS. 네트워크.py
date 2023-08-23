# dfs 코드
def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == 0:
                dfs(j)

    answer = 0
    visited = [0] * len(computers)
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    return answer