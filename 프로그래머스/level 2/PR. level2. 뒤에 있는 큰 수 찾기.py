# 20~24 시간초과
def solution(numbers):
    answer = []
    n = len(numbers)

    for i in range(n):
        if i == n - 1:
            answer.append(-1)
            break
        now = numbers[i]
        for j in range(i + 1, n):
            if numbers[j] > now:
                answer.append(numbers[j])
                break
        else:
            answer.append(-1)

    return answer

# 스택 응용 => 엄청 빨라진다
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and numbers[i] > numbers[stack[-1]]:
            now = stack.pop()
            answer[now] = numbers[i]
        stack.append(i)

    return answer