T = int(input())
for tc in range(1, T+1):
    N, D = map(int, input().split())
    ans = 0
    water = D * 2 + 1

    if N % water == 0:
        ans = N // water
    elif N % water != 0:
        ans = N // water + 1

    print(f'#{tc} {ans}')



