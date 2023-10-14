def solution(command):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # R을 만나면 dx, dy는 idx는 차례대로 이동하고, G를 만나면 거꾸로 이동
    # G를 만나면 idx 대로 실행하고, B를 만나면 숫자가 있는 좌표의 부호가 바뀐다

    idx = 0
    x = 0
    y = 0
    for order in command:
        if order == "R":
            idx = (idx + 1) % 4
        elif order == "L":
            idx = (idx + 3) % 4
        elif order == "G":
            x = x + dx[idx]
            y = y + dy[idx]
        else:
            if idx == 1 or idx == 3:
                x = x - dx[idx]
                y = y + dy[idx]
            elif idx == 0 or idx == 2:
                x = x + dx[idx]
                y = y - dy[idx]

    answer.append(x)
    answer.append(y)
    return answer