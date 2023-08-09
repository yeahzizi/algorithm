T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [input()[::-1] for _ in range(N)]
    code = {'0001101':0, '0011001':1, '0010011':2, '0111101':3,
            '0100011':4, '0110001':5, '0101111':6, '0111011':7,
            '0110111':8, '0001011':9}

    cnt = [0] * M
    for i in range(N):
        for j in range(M):
            cnt[j] += int(area[i][j])

    #print(cnt)

    n = 0
    for i in cnt:
        if i == 0:
            n += 1
        elif i != 0:
            break

    start = 0
    start += cnt[n]

    result = []
    for i in range(n, n+56):
        result.append(str(int(cnt[i]/start)))
    result = result[::-1]

    ans = []
    ans_str = ""
    for i in range(0, len(result)+1, 7):
        ans_str = "".join(result[i:i+7])
        ans.append(ans_str)
    #print(result)

    answer = []
    for i in range(len(ans)):
        for key, value in code.items():
            if key == ans[i]:
                answer.append(value)

    sum = 0
    for i in range(len(answer)):
        if i % 2 == 0:
            sum += 3 * answer[i]
        else:
            sum += answer[i]

    answer_sum = 0
    for i in range(len(answer)):
        answer_sum += int(answer[i])

    if sum % 10 == 0:
        print(f'#{tc}',answer_sum)
    else:
        print(f'#{tc}', 0)



















