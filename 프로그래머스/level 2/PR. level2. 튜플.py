def solution(s):
    answer = []
    s = s.replace("{", "").replace("}", "").split(",")
    combi = dict()

    for i in s:
        now = int(i)
        combi.setdefault(now, 0)
        combi[now] += 1

    combi = sorted(combi.items(), key=lambda x: x[1], reverse=True)
    for i, j in combi:
        answer.append(i)

    return answer