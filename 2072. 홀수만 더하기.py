T = int(input())
for tc in range(1, T + 1):
    N = map(int, input().split())
    total = 0

    for i in N: #N에 입력 받은 수가 홀수이면 총 값에 더한다.
        if i % 2 != 0:
            total += i


    print('#%d %d'%(tc, total))

