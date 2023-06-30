N = int(input())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

white = 0
blue = 0

def find(x, y, n):
    global white, blue
    check = array[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != array[i][j]:
                find(x, y, n//2)
                find(x, y+n//2, n//2)
                find(x+n//2, y, n//2)
                find(x+n//2, y+n//2, n//2)
                return

    if check == 0:
        white += 1
    else:
        blue += 1



find(0, 0, N)
print(white)
print(blue)

