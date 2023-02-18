N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(N-1):
    n, m = map(int, input().split())
    arr[n][m] += 1
    arr[m][n] += 1

visited = []
stack = [2]

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in range(N-1):
        if destination not in visited and arr[current][destination]:
            stack.append(destination)

print(visited)
