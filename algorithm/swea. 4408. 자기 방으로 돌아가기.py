for tc in range(1, int(input()) + 1):
    N = int(input())
    room_even = [0] * 402
    room_odd = [0] * 402

    for n in range(N):
        now, retry = map(int, input().split())

        if now < retry:
            for i in range(now, retry + 2):
                if i % 2 == 1:
                    room_odd[i] += 1
                if i != 0 and i % 2 == 0:
                    room_even[i - 1] += 1

        if now >= retry:
            for i in range(retry, now + 2):
                if i % 2 == 1:
                    room_odd[i] += 1
                if i != 0 and i % 2 == 0:
                    room_even[i - 1] += 1

    print(f'#{tc} {max(room_even)}')