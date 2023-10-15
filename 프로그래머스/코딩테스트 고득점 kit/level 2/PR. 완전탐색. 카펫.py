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

# version 2 => 가 더 구림


def solution(brown, yellow):
    answer = []
    whole = brown + yellow

    a, b = 0, 0
    for x in range(1, whole):
        if whole % x == 0:
            y = whole // x
        if x >= y and x > 2 and y > 2 and (x - 2) * (y - 2) == yellow and x * y == whole:
            a += x
            b += y

    answer.append(a)
    answer.append(b)
    return answer

# version 3 => 거꾸로 해야 빠르다!
def solution(brown, yellow):
    answer = []
    whole = brown + yellow

    a, b = 0, 0
    for x in reversed(range(whole)):
        if whole % x == 0:
            b = whole // x
            a = x
        if a >= b and a > 2 and b > 2 and (a - 2) * (b - 2) == yellow and a * b == whole:
            break

    answer.append(a)
    answer.append(b)
    return answer