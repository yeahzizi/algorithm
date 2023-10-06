import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
q = deque()
q.append(N)
visited[N] = 0

while q:
    now = q.popleft()
    if now == K:
        print(visited[now])
        break
    for i in (now-1, now+1, now*2):
        if 0 <= i <= 100000 and visited[i] == -1:
            visited[i] = visited[now] + 1
            q.append(i)

