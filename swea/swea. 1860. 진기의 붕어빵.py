T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort()
    bread = 0
    ans = "Impossible"

    for i in range(0, 11112):
        if i != 0 and i % M == 0:
            bread += K

        if i in person:
            if bread > 0:
                ans = "Possible"
                bread -= 1
            elif bread <= 0:
                ans = "Impossible"
                break

    print(f'#{tc} {ans}')











