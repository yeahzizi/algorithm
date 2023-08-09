for tc in range(int(input())):
    N = int(input())
    A_list = list(map(int, input().split()))
    minor = []
    ans = []

    for i in range(N):
        for j in range(i+1, N):
            minor.append(A_list[i] * A_list[j])

    str_list = list(map(str, minor))
    ans = []

    for i in str_list:
        for j in range(0, len(i)-1):
            if not int(i[j]) <= int(i[j+1]):
                break
        else:
            ans.append(i)

    ans_list = list(map(int, ans))

    if not ans:
        print(f'#{tc + 1}', -1)
    else:
        print(f'#{tc + 1} {max(ans_list)}')
















