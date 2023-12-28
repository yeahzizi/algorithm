def solution(n):
    answer = 0
    check = ''

    if n < 3:
        return n

    while n >= 3:
        num = n % 3
        check += str(num)
        n = n // 3
        if n < 3:
            check += str(n)

    check = check[::-1]
    for i, char in enumerate(check):
        answer += (3 ** i) * int(char)

    return answer