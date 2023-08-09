N = int(input())
T = int(input())
matrix = [[0] * (N + 1) for _ in range(N+ 1)]

for t in range(T):
    i, j = map(int, input().split())
    matrix[i][j] = 1
    matrix[j][i] = 1

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(N+1):
        if matrix[current][destination] and destination not in visited:
           stack.append(destination)

print(len(visited)-1)
