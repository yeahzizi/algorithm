def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        # x는 몫, y는 나머지
        x = i // n
        y = i % n
        if x == n - 1:
            answer.append(n)
        elif x < y:
            answer.append(x + 1 + (y - x))
        elif x >= y:
            answer.append(x + 1)

    return answer