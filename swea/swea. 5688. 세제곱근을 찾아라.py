T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = -1

    for x in range(1, 10**6+1):  #10의 18승까지 돌지 않도록, 10의 6승의 세제곱이 10의 18승이니 거기서 끊어준다.
        if N == (x * x * x):
            ans += (x+1)
            break

    print(f'#{tc} {ans}')





