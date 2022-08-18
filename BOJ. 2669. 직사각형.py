x1, y1, x2, y2 = [list(map(int, input().split())) for _ in range(4)]
x1, y1, x2, y2 = list(zip(x1, y1, x2, y2))
space = [[0] * 100 for _ in range(100)]


for n in range(4):
    for i in range(x1[n], x2[n]):
        for j in range(y1[n], y2[n]):
            space[i][j] += 1
            if space[i][j] >= 2:
                space[i][j] -= 1
area = 0
for s in range(100):
    area += sum(space[s])

print(area)






