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
