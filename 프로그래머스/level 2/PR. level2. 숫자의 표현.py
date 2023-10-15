def solution(n):
    answer = 0

    for i in range(1, n + 1):
        total = 0
        now = i
        total += now
        while total < n:
            now += 1
            total += now
        if total == n:
            answer += 1

    return answer