from itertools import combinations

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        if check(sum(i)) == True:
            answer += 1

    return answer