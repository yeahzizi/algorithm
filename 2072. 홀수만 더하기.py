T = int(input())
for test_case in range(1, T + 1):
    N = map(int, input().split())
    total = 0

    for i in N:
        if i % 2 != 0:
            total += i


    print('#%d %d'%(test_case, total))

