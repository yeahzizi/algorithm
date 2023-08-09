T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    h_list = list(map(int, input().split()))
    sum_list = []

    for i in range(1 << len(h_list)):
        result = []
        for j in range(len(h_list)):
            if i & (1 << j):
                result.append(h_list[j])

        if sum(result) - B >= 0:
            sum_list.append(sum(result) - B)

    print(f'#{tc} {min(sum_list)}')
