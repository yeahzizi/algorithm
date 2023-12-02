def solution(x, n):
    answer = []
    m = x * n

    if x > 0:
        for i in range(x, m + 1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, m - 1, x):
            answer.append(i)

    elif x == 0:
        while n > 0:
            answer.append(0)
            n -= 1

    return answer