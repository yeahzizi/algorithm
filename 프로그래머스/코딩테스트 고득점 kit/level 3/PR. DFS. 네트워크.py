# dfs 코드
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.34ms, 10MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.21ms, 10.4MB)
# 테스트 9 〉	통과 (0.08ms, 10MB)
# 테스트 10 〉	통과 (0.14ms, 10.1MB)
# 테스트 11 〉	통과 (1.02ms, 10.4MB)
# 테스트 12 〉	통과 (0.45ms, 10.2MB)
# 테스트 13 〉	통과 (0.47ms, 10.3MB)
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


#ver 2 빨라짐! 연결되어 있다고 dfs 함수에서 체크해주면 빨라짐
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.09ms, 10.1MB)
# 테스트 4 〉	통과 (0.07ms, 9.91MB)
# 테스트 5 〉	통과 (0.00ms, 9.98MB)
# 테스트 6 〉	통과 (0.18ms, 9.94MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.12ms, 10.2MB)
# 테스트 9 〉	통과 (0.14ms, 10.1MB)
# 테스트 10 〉	통과 (0.12ms, 10.1MB)
# 테스트 11 〉	통과 (0.57ms, 10.2MB)
# 테스트 12 〉	통과 (0.81ms, 10.2MB)
# 테스트 13 〉	통과 (0.25ms, 10MB)

def solution(n, computers):
    def dfs(x):
        visited[x] = 1
        for i in range(n):
            if computers[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(i)

    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1

    return answer