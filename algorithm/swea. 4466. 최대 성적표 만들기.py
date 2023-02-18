T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grade = list(map(int, input().split()))
    grade.sort(reverse=True)
    ans = 0
    cnt = 0

    for i in grade:
        ans += i
        cnt += 1
        if cnt == K:
            break

    print(f'#{tc} {ans}')
