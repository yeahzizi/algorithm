def solution(n, a, b):
    answer = 1

    while True:
        if max(a, b) - 1 == min(a, b) and min(a, b) % 2 == 1:
            break
        elif a % 2 == 1 and b % 2 == 1:
            a = a // 2 + 1
            b = b // 2 + 1
        elif a % 2 == 1 and b % 2 == 0:
            a = a // 2 + 1
            b = b // 2
        elif a % 2 == 0 and b % 2 == 1:
            a = a // 2
            b = b // 2 + 1
        elif a % 2 == 0 and b % 2 == 0:
            a = a // 2
            b = b // 2
        answer += 1

    return answer