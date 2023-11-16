def solution(numbers):
    answer = []
    n = len(numbers)

    for i in range(n):
        now = numbers[i]
        if now % 2 == 0:
            answer.append(now + 1)
        else:
            a = '0' + bin(now)[2:]
            for i in reversed(range(len(a))):
                if a[i] == "0":
                    a = "0b" + a[:i] + "1" + "0" + a[i + 2:]
                    break
            answer.append(int(a, 2))

    return answer