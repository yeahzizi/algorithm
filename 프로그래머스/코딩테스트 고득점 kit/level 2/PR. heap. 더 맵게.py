# 음식을 섞지 않고 기존 스코빌 점수가 이미 K값을 넘을 때 상황을 고려
# 아니면 18번 케이스만 틀리는 사태가 발생한다
# 효율성  테스트
# 테스트 1 〉	통과 (169.75ms, 16.2MB)
# 테스트 2 〉	통과 (395.61ms, 21.9MB)
# 테스트 3 〉	통과 (1780.67ms, 49.7MB)
# 테스트 4 〉	통과 (131.11ms, 14.9MB)
# 테스트 5 〉	통과 (3170.41ms, 51.9MB)

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

# version 2 => 예외에 늘 주의해야 함!!!
# 빨라진 경우도 아닌 경우도 있음
# 효율성  테스트
# 테스트 1 〉	통과 (176.46ms, 16.2MB)
# 테스트 2 〉	통과 (378.54ms, 21.8MB)
# 테스트 3 〉	통과 (2812.63ms, 49.7MB)
# 테스트 4 〉	통과 (196.66ms, 15MB)
# 테스트 5 〉	통과 (1873.91ms, 51.9MB)


import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if min(scoville) >= K:
        return 0

    while True:
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
        one = heapq.heappop(scoville)
        if one >= K:
            return answer
        else:
            two = heapq.heappop(scoville)
            heapq.heappush(scoville, (one + (two * 2)))
            answer += 1
