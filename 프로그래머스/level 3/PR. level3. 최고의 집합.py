def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    if s % n == 0:
        for i in range(n):
            answer.append(s // n)
        return answer
    else:
        now = s % n
        for i in range(n):
            if now == 0:
                answer.append(s // n)
            else:
                answer.append((s // n) + 1)
                now -= 1
    answer.sort()

    return answer