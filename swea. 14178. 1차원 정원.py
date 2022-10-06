#물이 갈 수 있는 범위가 N과 딱 나누어 떨어지면 나누어준 값이 답이 되고, 아니면 +1 한다.
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



