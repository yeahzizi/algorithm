def solution(n):
    answer = ''
    result = ['1', '2', '4']

    while n > 0:
        n -= 1
        answer = result[(n % 3)] + answer
        n = n // 3

    return answer


# 아래는 시간초과

def solution(n):
    answer = ''
    result = ['1', '2', '4']

    if n >= 4:
        for i in range(3, n):
            now = result[(i // 3) - 1] + result[(i % 3)]
            result.append(now)

    return result[n - 1]