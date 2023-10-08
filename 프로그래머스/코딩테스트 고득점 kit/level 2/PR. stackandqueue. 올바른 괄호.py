def solution(s):
    answer = True
    s = list(s)
    stack = []

    while s:
        now = s.pop()
        if not stack and now == "(":
            return False
            break
        if now == ")" and stack and stack[-1] == "(":
            stack.pop()
            continue
        if now == "(" and stack and stack[-1] == ")":
            stack.pop()
            continue
        else:
            stack.append(now)

    if not stack:
        answer = True
    else:
        answer = False

    return answer