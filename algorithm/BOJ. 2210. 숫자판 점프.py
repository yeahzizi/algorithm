#델타검색 + dfs(재귀 + 인접행렬)
#좌표의 모든 수가 출발점이 된다.

def dfs(x, y, six_number):
    if len(six_number) == 6:
        if six_number not in result:
            result.append(six_number)
        return

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for s in range(4):
        dx_x = x + dx[s]
        dy_y = y + dy[s]

        if 0 <= dx_x < 5 and 0 <= dy_y < 5:
            dfs(dx_x, dy_y, six_number + number[dx_x][dy_y])

#입력
number = [list(map(str, input().split())) for _ in range(5)] #2차원 입력 받기
result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, number[i][j])

print(len(result))

