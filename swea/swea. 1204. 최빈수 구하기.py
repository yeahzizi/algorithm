T = int(input())
for tc in range(1, T+1):
    N = int(input())
    student = list(map(int, input().split()))
    cnt = [0] * 101
    idx = []

    for i in student:
        cnt[i] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            idx.append(i)


    print(f'#{tc}', idx[-1])