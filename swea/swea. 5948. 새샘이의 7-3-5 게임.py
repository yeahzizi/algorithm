for tc in range(1, int(input())+1):
    num = list(map(int, input().split()))
    ans = []

    for i in num:
        for j in num:
            for k in num:
                if i != j and j != k and i != k:
                    ans.append(i+j+k)

    ans = set(ans)
    ans = list(ans)
    ans.sort()

    print(f'#{tc} {ans[-5]}')
