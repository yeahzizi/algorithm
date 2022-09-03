import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))
    profit = 0
    end = num[-1]

    for i in range(N-2, -1, -1):
        if num[i] > end:
            end = num[i] #마지막 값으로 갱신(마지막 값은 항상 구매하지 않으므로)

        else:
            profit += end - num[i]
        #만약에 num[i]이 end보다 크면 구매하지 않을 것이므로, 작을 때만 end에서 빼준 뒤 이익에 더한다.

    print(f'#{tc} {profit}')

    #end를 max 값으로 생각하면 더 쉽게 이해 가능(마지막 값을 max로 가정하고 큰 값이 나오면 갱신)





