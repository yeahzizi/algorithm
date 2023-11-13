# 너무 어렵게 생각 말기..
def solution(order):
    answer = 0
    n = len(order)
    stack = []  # 보조
    idx = 0

    for i in range(1, n + 1):
        stack.append(i)
        while stack and order[idx] == stack[-1]:
            stack.pop()
            idx += 1
            answer += 1

    return answer