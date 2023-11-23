def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n + 1)]
    num = 1
    x, y = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1

    return sum(triangle, [])  # 리스트를 합침