# q 자체는 리스트이기 때문에 리스트 함수를 사용할 수 있다

import heapq

def solution(operations):
    answer = []
    q = []

    for oper in operations:
        x, num = oper.split()
        num = int(num)
        if x == "I":
            heapq.heappush(q, num)
        elif x == "D" and num == 1:
            if len(q) != 0:
                value = max(q)
                q.remove(value)
        else:
            if len(q) != 0:
                heapq.heappop(q)
    if not q:
        return [0, 0]
    else:
        return [max(q), heapq.heappop(q)]
