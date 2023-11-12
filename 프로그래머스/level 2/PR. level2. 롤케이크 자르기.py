# 시간초과
def solution(topping):
    answer = 0
    n = len(topping)

    for i in range(1, n):
        one, two = set(topping[:i]), set(topping[i:])
        if len(one) == len(two):
            answer += 1

    return answer