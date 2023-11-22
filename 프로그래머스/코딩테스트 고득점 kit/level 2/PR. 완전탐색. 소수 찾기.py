from itertools import permutations

def prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    num = []
    answer = 0

    for i in range(1, len(numbers) + 1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))

    for i in num:
        for j in i:
            if j[0] != "0":
                if prime(int(j)):
                    print(j)
                    answer += 1

    return answer

#version 2
from itertools import permutations


def prime(check):
    if check < 2:
        return False

    for i in range(2, (check // 2) + 1):
        if check % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num = []

    for i in range(1, len(numbers) + 1):
        num.append(list(set(map(''.join, permutations(numbers, i)))))

    for i in num:
        for j in i:
            if j[0] != "0":
                if prime(int(j)):
                    answer += 1

    return answer
