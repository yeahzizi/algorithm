T = int(input())
for tc in range(1, T+1):
    N = int(input())
    start = 0     #속도를 구해줄 값
    distance = 0  #거리를 구해줄 값

    for i in range(N):
        speed = input()   #문자열로 입력 받은 다음 슬라이싱 할 것

        if speed[:1] == "1":
            start += int(speed[1:])
            distance += start  #속도를 계속 더하면 총 거리가 된다.
            continue
        elif speed[:1] == "2":
            start -= int(speed[1:])
            if start < 0:  #문제 조건에 따라 스피드가 0이면 마이너스가 되는 것이 아니라,
                start = 0  #속도가 0이 된다.
            distance += start
            continue
        elif speed[:1] == "0":
            start = start
            distance += start
            continue

    print(f'#{tc} {distance}')














