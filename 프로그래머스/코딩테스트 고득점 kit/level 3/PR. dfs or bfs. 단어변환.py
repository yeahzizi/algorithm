# bfs + 뎁스 활용한 문제

from collections import deque

def solution(begin, target, words):
    n = len(words)
    answer = 0
    q = deque()
    q.append((begin, 0))
    check = [0] * n

    while q:
        now, level = q.popleft()
        if now == target:
            return level
        for i in range(n):
            cnt = 0
            if not check[i]:
                for j in range(len(words[i])):
                    if now[j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    q.append((words[i], level + 1))
                    check[i] = 1

    return answer