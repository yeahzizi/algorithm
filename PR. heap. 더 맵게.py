# 음식을 섞지 않고 기존 스코빌 점수가 이미 K값을 넘을 때 상황을 고려
# 아니면 18번 케이스만 틀리는 사태가 발생한다

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return answer

    while True:
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        spicy = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, spicy)
        answer += 1
        if scoville[0] >= K:
            break

    return answer