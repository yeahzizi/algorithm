import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))
    profit = 0
    end = num[- 1]

    for i in range(N-2, -1, -1):
        if num[i] > end:
            end = num[i] #마지막 값으로 갱신(마지막 값은 항상 구매하지 않으므로)

        else:
            profit += end - num[i]

    print(f'#{tc} {profit}')






