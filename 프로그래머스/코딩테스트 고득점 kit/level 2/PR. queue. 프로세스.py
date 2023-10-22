# 어렵게 생각하지 말자
def solution(priorities, location):
    answer = 0
    q = []

    for i in range(len(priorities)):
        q.append([priorities[i], i])

    while q:
        m = max(q)
        value, idx = q.pop(0)
        if value < m[0]:
            q.append([value, idx])
        else:
            answer += 1
            if idx == location:
                return answer

    return answer