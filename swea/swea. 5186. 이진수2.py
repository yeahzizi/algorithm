T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ""

    for i in range(1, 13):
        if N >= 2**(-i):
            N -= 2**(-i)
            ans += str(1)
        else:
            ans += str(0)
        if N == 0:
            break
    if N > 0:
        print(f'#{tc}', "overflow")
    else:
        print(f'#{tc} {ans}')
