N = int(input())

triangle = []
for i in range(N):
    triangle.append([0] + list(map(int, input().split())) + [0])


for i in range(1, N):
    for j in range(1, i+2):
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])


print(max(triangle[-1]))
