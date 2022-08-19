T = int(input())
space = [[0] * 100 for _ in range(100)]

for t in range(T): #반복문을 이용해 space 내부 해당 범위에 1씩 더한다.
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            space[i][j] += 1
            if space[i][j] == 2: #2이상이면 1씩 뺀다.
                space[i][j] -= 1
area = 0
for i in range(100): #반복문을 이용해 space 전체 합을 구한다.
    for j in range(100):
        area += space[i][j]
print(area)


