# 효율성 테스트만 통과 못함

def solution(n, works):
    answer = 0

    while True:
        if n == 0:
            break
        now = max(works)
        if now == 0:
            return 0
        works.append(now - 1)
        works.remove(now)
        n -= 1

    for i in works:
        answer += i * i

    return answer

# 힙은 진짜 빠르다
# -1 을 곱해줘서 최대힙을 구현함

import heapq


def solution(n, works):
    answer = 0

    for i in range(len(works)):
        works[i] = -1 * works[i]

    heapq.heapify(works)
    for i in range(n):
        now = heapq.heappop(works)
        if now == 0:
            return 0
        heapq.heappush(works, now + 1)

    for i in works:
        answer += i * i

    return answer