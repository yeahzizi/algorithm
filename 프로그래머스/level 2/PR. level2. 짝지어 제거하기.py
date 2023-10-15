def solution(s):
    answer = 0
    s = list(s)
    stack = []
    stack.append(s.pop(0))

    for now in s:
        if not stack:
            stack.append(now)
        else:
            if now == stack[-1]:
                stack.pop()
            else:
                stack.append(now)

    if len(stack) == 0:
        return 1

    return answer