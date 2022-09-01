T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = 0
    distance = 0

    for i in range(N):
        speed = input()

        if speed[:1] == "1":
            start += int(speed[1:])
            distance += start
            continue
        elif speed[:1] == "2":
            start -= int(speed[1:])
            if start < 0:
                start = 0
            distance += start
            continue
        elif speed[:1] == "0":
            start = start
            distance += start
            continue

    print(f'#{tc} {distance}')














