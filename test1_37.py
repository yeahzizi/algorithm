#37개 맞은 거
T = int(input())
for tc in range(1, T+1):
    N, Kmin, Kmax = map(int, input().split())
    score = list(map(int, input().split()))

    for i in range(len(score)-1):
        for j in range(len(score)-1):
            if score[j] > score[j + 1]:
                score[j], score[j + 1] = score[j + 1], score[j]

    T1, T2 = 0, 0
    cnt1 = []
    cnt2 = []
    cnt3 = []

    for i in range(len(score)):
        for j in range(i+1, len(score)):
            if score[i] < score[j] and N // 3 <= min(len(score[:i]), len(score[i:j]), len(score[j:])):
                T1, T2 = score[i], score[j]

    for k in range(len(score)):
        if score[k] < T1:
            cnt1.append(score[k])
        elif T1 <= score[k] < T2:
            cnt2.append(score[k])
        else:
            cnt3.append(score[k])

    if Kmin <= len(cnt1) <= Kmax and Kmin <= len(cnt2) <= Kmax and Kmin <= len(cnt3) <= Kmax:
        print(f'#{tc} {max(len(cnt1), len(cnt2), len(cnt3)) - min(len(cnt1), len(cnt2), len(cnt3))}')
    else:
        print(f'#{tc} -1')


"""
    
"""




"""
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5
"""


