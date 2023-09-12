import heapq
import sys
input = sys.stdin.readline

def dik(cost, x, y):
    q = []
    heapq.heappush(q, (cost, x, y))
    check[0][0] = 0

    while q:
        cost, i, j = heapq.heappop(q)

        if i == N-1 and j == N-1:
            print(f'Problem {cnt}: {check[i][j]}')

        for d in range(4):
            di = i + dx[d]
            dj = j + dy[d]
            if 0 <= di < N and 0 <= dj < N:
                new_cost = cost + cave[di][dj]
                if new_cost < check[di][dj]:
                    check[di][dj] = new_cost
                    heapq.heappush(q, (new_cost, di, dj))
cnt = 0
while True:
    N = int(input())
    if N == 0:
        break
    cave = []
    for _ in range(N):
        cave.append(list(map(int, input().split())))

    INF = int(1e9)
    check = [[INF] * (N+1) for _ in range(N+1)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    cnt += 1
    dik(cave[0][0], 0, 0)
