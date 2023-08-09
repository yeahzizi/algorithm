N = int(input())

array = []
for i in range(N):
    array.append(list(input()))

result = ''

def quad(x, y, n):
    global result
    check = array[x][y]

    for j in range(x, x+n):
        for k in range(y, y+n):
            if check != array[j][k]:
                check = -1
                break

    if check == -1:
        result += "("
        quad(x, y, n//2)
        quad(x, y+n//2, n//2)
        quad(x+n//2, y, n//2)
        quad(x+n//2, y+n//2, n//2)
        result += ")"

    elif check == "1":
        result += "1"

    elif check == "0":
        result += "0"



quad(0, 0, N)
print(result)