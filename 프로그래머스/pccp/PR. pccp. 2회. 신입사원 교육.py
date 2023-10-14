# 재귀 시간초과
def check(ability):
    ability.sort()
    a = ability[0]
    b = ability[1]

    ability[ability.index(a)] = a + b
    ability[ability.index(b)] = a + b

    return ability


def solution(ability, number):
    answer = 0

    for i in range(number):
        ability = check(ability)

    return sum(ability)


# 힙을 사용하면 이렇게 빠르다..
import heapq


def solution(ability, number):
    answer = 0
    heapq.heapify(ability)

    while number > 0:
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)

        heapq.heappush(ability, a + b)
        heapq.heappush(ability, a + b)
        number -= 1

    return sum(ability)