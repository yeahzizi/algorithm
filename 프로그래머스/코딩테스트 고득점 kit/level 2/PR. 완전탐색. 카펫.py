def solution(brown, yellow):
    answer = []
    all_color = brown + yellow

    a, b = 0, 0
    for i in reversed(range(all_color)):
        if i > 0 and all_color % i == 0:
            a = i
            b = all_color // i
            if a > 2 and b > 2 and a >= b and yellow % (i - 2) == 0 and yellow % (b - 2) == 0:
                answer.append(a)
                answer.append(b)

    return answer