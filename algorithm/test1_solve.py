T = int(input())
for tc in range(1, T+1):
    N, Kmin, Kmax = map(int, input().split())
    score = list(map(int, input().split()))

    score.sort()
    ans = 100

    for i in range(min(score), len(score)):
        for j in range(i+1, len(score)):
            A, B, C = 0, 0, 0
            if score[i] < score[j]:
                for k in range(N):
                    if score[k] < i:
                        A += 1
                    elif i <= score[k] < j:
                        B += 1
                    else:
                        C += 1

                if min(A, B, C) < Kmin and max(A, B, C) > kmax:
                    continue
                else:
                    ans = min(ans, max(A, B, C) - min(A, B, C))

    if ans == 100 or max(A, B, C) * 3 < N or min(A, B, C) * 3 > N:
        print(f'{tc+1} -1')
    else:
        print(f'{tc + 1} {ans}')




