# 테스트 11부터 시간초과

def solution(gems):
    answer = []
    gem = set(gems)
    n = len(gems)

    idx = 0
    while idx < n:
        arr = []
        for i in range(idx, n):
            arr.append(gems[i])
            if set(arr) == gem:
                answer.append([idx + 1, i + 1])

        idx += 1
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]