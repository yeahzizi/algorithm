# 소수 판별 알고리즘
# 2부터 sqrt() 까지 나누었을 때 한번이라도 맞아 떨어지면
# 소수가 아님

import math


def solution(n, k):
    answer = 0
    word = ""
    while n:
        word += str(n % k)
        n = n // k

    word = word[::-1]
    word = word.split("0")

    for w in word:
        if len(w) == 0:
            continue
        elif int(w) < 2:
            continue
        sosu = True
        for i in range(2, int(math.sqrt(int(w)) + 1)):
            if int(w) % i == 0:
                sosu = False
                break
        if sosu:
            answer += 1

    return answer