from collections import deque

for t in range(int(input())):
    N = int(input()) # 편의점 개수
    store = []
    h1, h2 = map(int, input().split())
    for i in range(N):
        c1, c2 = map(int, input().split())
        store.append((c1, c2))
    r1, r2 = map(int, input().split())
    store.append((r1, r2))


    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            a, b = q.popleft()
            for cx, cy in store:
                if abs(cx-a) + abs(cy-b) <= 1000:
                    q.append((cx, cy))
                    store.remove((cx, cy))

                    if cx == r1 and cy == r2:
                        return "happy"

        return "sad"


    print(bfs(h1, h2))
