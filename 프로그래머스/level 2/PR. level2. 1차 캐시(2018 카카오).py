# 엣지 케이스 파악하는 것이 중요!
# 엣지 케이스 정리하기

def solution(cacheSize, cities):
    answer = 5
    if cacheSize == 0:
        return len(cities) * 5
    k = cities.pop(0)
    k = k.lower()
    q = [k]

    while cities:
        now = cities.pop(0)
        now = now.lower()
        if now in q:
            answer += 1
            q.append(now)
            if cacheSize < len(q):
                q.remove(now)
        else:
            answer += 5
            q.append(now)
            if cacheSize < len(q):
                q.pop(0)

    return answer