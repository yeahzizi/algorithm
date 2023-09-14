N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

check = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
