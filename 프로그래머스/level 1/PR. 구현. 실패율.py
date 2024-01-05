def solution(N, stages):
    answer = []
    stages.sort()
    check = dict()
    m = len(stages)

    for i in range(1, N + 1):
        check.setdefault(i, 0)

    for i in stages:
        if i <= N:
            check[i] += 1

    for i, j in check.items():
        if m > 0:
            answer.append((i, j / m))
            m -= j
        else:
            answer.append((i, 0))

    answer.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in answer]