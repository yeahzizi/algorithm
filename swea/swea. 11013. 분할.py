for tc in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    min_diff = 999999
    cal = 0

    for i in range(1, N-1):
        for j in range(i+1, N):
            cal = max(sum(num[0:i]), sum(num[i:j]), sum(num[j:N])) - min(sum(num[0:i]), sum(num[i:j]), sum(num[j:N]))

            if cal <= min_diff:
                min_diff = cal

    print(f'#{tc} {min_diff}')

