n = int(input())
a, b = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
m = int(input())
for m in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

stack = [a]
visited = [0]*(n+1)
visited[a] = 1

while stack:
    current = stack.pop()
    for destination in range(n+1):
        if matrix[current][destination] and not visited[destination]:
            visited[destination] = visited[current] + 1
            stack.append(destination)

print(visited[b]-1)