T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))
    count = 0
    max_count = 0

    for i in num:
        if i == 1:
            count += 1
            continue
        elif i == 0:
            if max_count < count:
                max_count = count
                count = 0
    if max_count < count:
        max_count = count

    print(f'#{tc} {max_count}')






