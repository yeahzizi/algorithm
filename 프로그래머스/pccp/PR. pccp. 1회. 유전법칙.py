# 재귀를 이렇게 풀 수도 있다!

def check(x, y):
    if x == 1:
        return "Rr"
    parent = check(x - 1, (y - 1) // 4 + 1)

    if parent == "RR" or parent == "rr":
        return parent
    elif parent == "Rr":
        if (y - 1) % 4 == 0:
            return "RR"
        elif (y - 1) % 4 == 1 or (y - 1) % 4 == 2:
            return "Rr"
        elif (y - 1) % 4 == 3:
            return "rr"


def solution(queries):
    answer = []

    for i, j in queries:
        answer.append(check(i, j))

    return answer