# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10MB)
# 테스트 4 〉	통과 (0.33ms, 10.4MB)
# 테스트 5 〉	통과 (1.30ms, 10.4MB)
# 테스트 6 〉	통과 (0.36ms, 10.1MB)
# 테스트 7 〉	통과 (1.39ms, 10.5MB)
# 테스트 8 〉	통과 (0.28ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.19ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (44.20ms, 17.9MB)
# 테스트 2 〉	통과 (32.21ms, 16.1MB)
# 테스트 3 〉	통과 (51.64ms, 18.9MB)
# 테스트 4 〉	통과 (45.86ms, 18MB)
# 테스트 5 〉	통과 (41.85ms, 17.4MB)
# 테스트 6 〉	통과 (47.90ms, 19.3MB)
# 테스트 7 〉	통과 (43.19ms, 18.6MB)
# 테스트 8 〉	통과 (39.30ms, 17.1MB)
# 테스트 9 〉	통과 (37.47ms, 17.3MB)
# 테스트 10 〉	통과 (43.46ms, 18.7MB)

def solution(triangle):
    answer = 0
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]

    if len(triangle) > 1:
        for i in range(2, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[len(triangle) - 1])

# 살짝 느려짐 예전에는 j == i 라는 씽크빅 코드를 써서 좀 빨랐음
def solution(triangle):
    n = len(triangle)
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]

    if n > 1:
        for i in range(2, n):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(dp[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[n - 1])