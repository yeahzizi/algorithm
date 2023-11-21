def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], x[1]))
    m = -30001

    for i, j in routes:
        if i > m:
            answer += 1
            m = j
        m = min(m, j)

    return answer