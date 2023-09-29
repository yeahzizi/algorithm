# 방향을 어떻게 푸는지가 이 문제의 관건!
# 나는 북쪽 => 0, 동쪽 => 1, 남쪽 => 2, 서쪽 => 3 이렇게 풀었음
# visited = set() 이런 거 좋다
# 문제는 너무 오래 걸림^^

for t in range(int(input())):
    order = list(input())
    x, y, direction = 0, 0, 0
    visited = set()

    for i in order:
        if i == "L":
            if direction == 0:
                direction = 3
            else:
                direction -= 1
        if i == "R":
            direction += 1
        if i == "F":
            if direction % 4 == 0:
                y += 1
            elif direction % 4 == 1:
                x += 1
            elif direction % 4 == 2:
                y -= 1
            elif direction % 4 == 3:
                x -= 1
        if i == "B":
            if direction % 4 == 0:
                y -= 1
            elif direction % 4 == 1:
                x -= 1
            elif direction % 4 == 2:
                y += 1
            elif direction % 4 == 3:
                x += 1

        visited.add((x, y))

    max_x, max_y = 0, 0
    min_x, min_y = 0, 0

    for x, y in visited:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    print(abs(max_x - min_x) * abs(max_y - min_y))


