import heapq


def solution(menu, order, k):
    answer = 0
    q = []
    heapq.heapify(q)
    start, end = -k, 0

    for i in order:
        start += k
        end = (start if end < start else end) + menu[i]
        heapq.heappush(q, end)

        while q:
            out = heapq.heappop(q)
            if out > start:
                heapq.heappush(q, out)
                break

        answer = max(answer, len(q))

    return answer