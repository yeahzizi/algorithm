for tc in range(10):
    N = int(input())
    S = [list(input()) for _ in range(8)]
    S_zip = list(map(list, zip(*S)))
    print(S_zip)

    ans = 0

    for i in range(8):
        for j in range(8-N+1): #범위 주의하기
            if S[i][j:j+N] == S[i][j:j+N][::-1]:
                ans += 1
                print(S[i][j:j+N])


    for i in range(8):
        for j in range(8-N+1):
            if S_zip[i][j:j+N] == S_zip[i][j:j+N][::-1]:
                ans += 1
                print(S_zip[i][j:j+N])


    print(f'#{tc+1} {ans}')