def solution(numbers):
    answer = 0
    numbers.sort()
    check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in check:
        if i not in numbers:
            answer += i
    return answer