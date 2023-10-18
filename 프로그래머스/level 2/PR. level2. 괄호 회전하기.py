def solution(s):
    answer = 0
    for i in range(len(s)):
        now = s[i:] + s[:i]
        while True:
            n = len(now)
            now = now.replace("()", "")
            now = now.replace("{}", "")
            now = now.replace("[]", "")
            if now == '':
                answer += 1
                break
            if len(now) == n:
                break

    return answer