# 진짜 간단한 실수에서 헤매다 ㅎㅎ
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.32ms, 10.1MB)
# 테스트 3 〉	통과 (0.15ms, 10.1MB)
# 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.15ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.1MB)
# 테스트 9 〉	통과 (0.09ms, 10.2MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
import math


def solution(progresses, speeds):
    answer = []
    finish = []

    for i in range(len(progresses)):
        for j in range(len(speeds)):
            if i == j:
                work = math.ceil((100 - progresses[i]) / speeds[j])
                finish.append(work)

    cnt = 1
    max_num = finish[0]
    for i in range(1, len(finish) + 1):
        if i == len(finish):
            answer.append(cnt)
            break
        if max_num < finish[i]:
            answer.append(cnt)
            cnt = 1
            max_num = finish[i]
        else:
            cnt += 1

    return answer

# only stack  => 훨씬 빨라짐
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.05ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)

def solution(progresses, speeds):
    answer = []
    cnt = []
    n = len(progresses)
    for i in range(n):
        now = 100 - progresses[i]
        if now % speeds[i] == 0:
            cnt.append(now // speeds[i])
            continue
        cnt.append((now // speeds[i]) + 1)

    ans = 1
    for i in range(len(cnt)):
        if i == len(cnt) - 1:
            answer.append(ans)
            break
        elif cnt[i] >= cnt[i + 1]:
            cnt[i + 1] = cnt[i]
            ans += 1
        else:
            answer.append(ans)
            ans = 1

    return answer
