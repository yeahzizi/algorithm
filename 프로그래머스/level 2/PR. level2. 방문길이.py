def solution(dirs):
    visited = set()
    x, y = 0, 0

    for i in dirs:
        if i == "U":
            nx, ny = x, y + 1
        elif i == "D":
            nx, ny = x, y - 1
        elif i == "R":
            nx, ny = x + 1, y
        else:
            nx, ny = x - 1, y

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            move = ((x, y), (nx, ny))
            visited.add(move)
            visited.add((move[1], move[0]))
            x, y = nx, ny

    return len(visited) // 2