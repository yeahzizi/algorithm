#테스트 1 〉	통과 (18.47ms, 11.1MB)
#테스트 2 〉	통과 (16.24ms, 11.1MB)

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

# 재풀이
# 테스트 1 〉	통과 (8.87ms, 10.4MB)
# 테스트 2 〉	통과 (8.93ms, 10.4MB)

def solution(s):
    answer = True
    stack = []

    for case in s:
        if case == "(":
            stack.append(case)
        elif case == ")":
            if not stack or stack[-1] == ")":
                return False
                break
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False