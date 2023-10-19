# 테스트 1 〉	통과 (0.07ms, 10.2MB)
# 테스트 2 〉	통과 (0.29ms, 10.1MB)
# 테스트 3 〉	통과 (0.13ms, 10.4MB)
# 테스트 4 〉	통과 (0.10ms, 10.2MB)
# 테스트 5 〉	통과 (0.25ms, 10.1MB)
# 테스트 6 〉	통과 (0.20ms, 10.2MB)
# 테스트 7 〉	통과 (0.07ms, 10.4MB)
# 테스트 8 〉	통과 (0.01ms, 10MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.05ms, 10.2MB)
# 테스트 11 〉	통과 (0.25ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10MB)
# 테스트 13 〉	통과 (0.28ms, 10.2MB)
# 테스트 14 〉	통과 (0.16ms, 10.4MB)
# 테스트 15 〉	통과 (0.34ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.1MB)

def solution(citations):
    citations.sort()
    answer = 0

    cnt = 0
    for i in citations:
        if i == 0:
            cnt += 1
            if cnt == len(citations):
                return 0

    for i in range(501):
        h = len(citations[i:])
        if citations[i] >= h:
            return h
            break

# 훨씬 느려졌지만..내힘으로 품
def solution(citations):
    citations.sort()
    cnt = [0] * (max(citations) + 1)
    for i in citations:
        cnt[i] += 1
        if cnt[i] == len(citations):
            return 0

    answer = 0
    for i in range(len(cnt)):
        if i <= sum(cnt[i:]):
            answer = max(i, answer)

    return answer
