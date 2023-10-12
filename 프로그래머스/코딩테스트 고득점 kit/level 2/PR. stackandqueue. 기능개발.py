# 진짜 간단한 실수에서 헤매다 ㅎㅎ
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
