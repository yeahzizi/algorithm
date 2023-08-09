#더러운 풀이..
#정렬도 따로 하고 경우의 수도 많이 따져야 했다..

def solution(n, lost, reserve):
    student = []
    for i in range(n):
        if i + 1 not in lost:
            student.append(i + 1)

    lost.sort()
    reserve.sort()

    for i in reserve:
        if i not in student:
            student.append(i)
        elif i - 1 >= 1 and i - 1 not in student and i - 1 not in reserve:
            student.append(i - 1)
        elif i + 1 <= n and i + 1 not in student and i + 1 not in reserve:
            student.append(i + 1)

    return len(set(student))