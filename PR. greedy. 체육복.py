# 이렇게 풀면 안됨
def solution(n, lost, reserve):
    answer = 0

    student = []
    for i in range(n):
        if i + 1 not in lost:
            student.append(i + 1)

    return answer