x1, y1, x2, y2 = [list(map(int, input().split())) for _ in range(4)]
x1, y1, x2, y2 = list(zip(x1, y1, x2, y2))  #zip을 이용해 x좌표끼리 y좌표끼리 모은다.
space = [[0] * 100 for _ in range(100)]


for n in range(4): #반복문을 이용해 space 내부 해당 범위에 1씩 더한다.
    for i in range(x1[n], x2[n]):
        for j in range(y1[n], y2[n]):
            space[i][j] += 1
            if space[i][j] >= 2:  #2이상이면 1씩 뺀다(3인 경우에는 2를 빼면 중복으로 빠지므로 3도 1만 뺀다.)
                space[i][j] -= 1
area = 0
for s in range(100): #반복문을 이용해 space 전체 합을 구한다.
    area += sum(space[s])

print(area)






