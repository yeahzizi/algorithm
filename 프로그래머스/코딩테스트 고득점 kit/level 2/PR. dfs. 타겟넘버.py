# 여러 방법으로 풀어보기

def solution(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, value):
        if idx == n:
            if value == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, value + numbers[idx])
            dfs(idx + 1, value - numbers[idx])

    dfs(0, 0)

    return answer
