T = int(input())
space = [[0] * 100 for _ in range(100)]

for t in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            space[i][j] += 1
            if space[i][j] == 2:
                space[i][j] -= 1
area = 0
for i in range(100):
    for j in range(100):
        area += space[i][j]
print(area)


