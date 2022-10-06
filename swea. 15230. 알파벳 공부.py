T = int(input())
for tc in range(1, T+1):
    S = input()
    alp = ["abcdefghijklmnopqrstuvwxyz"]
    ans = 0

    for i in range(len(S)):
        if alp[0][i] == S[i]:
            ans += 1
        else:
            break

    print(f'#{tc} {ans}')