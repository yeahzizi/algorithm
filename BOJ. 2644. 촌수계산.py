n = int(input())
a, b = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
m = int(input())
for m in range(m):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

stack = [a]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)
    for destination in range(n+1):
        if matrix[current][destination] and destination not in visited:
            stack.append(destination)

print(visited)
print(matrix)
if b not in visited:
    print(-1)
else:
    