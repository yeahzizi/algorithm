for _ in range(int(input())):
    N = int(input())
    stock = list(map(int, input().split()))

    ans = 0
    standard = stock[N-1]
    for i in reversed(range(N-1)):
        if standard > stock[i]:
            ans += (standard - stock[i])

        else:
            standard = stock[i]

    print(ans)


