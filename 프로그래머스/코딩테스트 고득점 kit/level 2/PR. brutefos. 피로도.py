# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.08ms, 10.3MB)
# 테스트 5 〉	통과 (0.48ms, 10.3MB)
# 테스트 6 〉	통과 (3.34ms, 10.3MB)
# 테스트 7 〉	통과 (30.64ms, 10.2MB)
# 테스트 8 〉	통과 (31.40ms, 10.1MB)
# 테스트 9 〉	통과 (0.06ms, 10.3MB)
# 테스트 10 〉	통과 (3.16ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (28.64ms, 10.1MB)
# 테스트 13 〉	통과 (25.35ms, 10.3MB)
# 테스트 14 〉	통과 (29.40ms, 10.2MB)
# 테스트 15 〉	통과 (21.90ms, 10.1MB)
# 테스트 16 〉	통과 (2.67ms, 10.1MB)
# 테스트 17 〉	통과 (27.56ms, 10.1MB)
# 테스트 18 〉	통과 (0.04ms, 10.3MB)
# 테스트 19 〉	통과 (0.07ms, 10.2MB)

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

# 느려졌지만..내가 풀었다!
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    arr = list(permutations(dungeons, len(dungeons)))

    for case in arr:
        k2 = k
        cnt = 0
        while case:
            for need, waste in case:
                if need <= k2 and waste <= k2:
                    k2 -= waste
                    cnt += 1
            break
        answer = max(answer, cnt)

    return answer