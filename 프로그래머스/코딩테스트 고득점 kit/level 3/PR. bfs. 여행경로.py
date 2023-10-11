from collections import deque


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    q = deque([(["ICN"], tickets)])

    while q:
        now, remain = q.popleft()
        if not remain:
            answer = now
            break

        valid = -1
        for i in range(len(remain)):
            if now[-1] == remain[i][0]:
                valid = i
                break

        if valid == -1:
            continue

        while valid < len(remain) and remain[valid][0] == now[-1]:
            q.append((now + [remain[valid][1]], remain[:valid] + remain[valid + 1:]))
            valid += 1

    return answer