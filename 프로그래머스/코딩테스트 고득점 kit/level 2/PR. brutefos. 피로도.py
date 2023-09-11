from itertools import permutations

def solution(k, dungeons):
    answer = -1
    array = permutations(dungeons, len(dungeons))

    for i in array:
        cnt = 0
        k2 = k
        for x, y in i:
            if x > k2:
                continue
            k2 = k2 - y
            cnt += 1
        answer = max(answer, cnt)

    return answer
