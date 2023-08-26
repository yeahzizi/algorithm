import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, city = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (N+1)

def dijkstra(city):
    q = []
    heapq.heappush(q, (0, city))
    distance[city] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(city)

cnt = 0
total = 0
for i in range(1, N+1):
    if distance[i] > 0 and distance != INF:
        cnt += 1
        total = max(total, distance[i])

print(cnt, total)