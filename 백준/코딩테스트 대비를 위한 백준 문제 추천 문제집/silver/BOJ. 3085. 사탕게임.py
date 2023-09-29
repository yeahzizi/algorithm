N = int(input())
candy = []
for _ in range(N):
    candy.append(list(input()))


def check(arr):
    n = len(arr)
    answer = 1
    for i in range(n):
        cnt = 1
        #행 확인
        for j in range(1, n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1

            if answer < cnt:
                answer = cnt

        #열 확인
        cnt = 1
        for j in range(1, n):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
            else:
                cnt = 1
            if answer < cnt:
                answer = cnt

    return answer




answer = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            cnt = check(candy)

            if cnt > answer:
                answer = cnt

            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        if i+1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            cnt = check(candy)

            if cnt > answer:
                answer = cnt

            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]


print(answer)






