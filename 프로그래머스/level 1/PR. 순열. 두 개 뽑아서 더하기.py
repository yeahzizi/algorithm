from itertools import permutations

def solution(numbers):
    answer = []

    for i in permutations(numbers, 2):
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer