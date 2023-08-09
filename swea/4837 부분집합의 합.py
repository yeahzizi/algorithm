T = int(input())
A = [i for i in range(1, 13)]
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0

    for i in range(1 << len(A)):  # 0부터 2^n - 1 만큼 돌려줌 > 1>>n은 부분 집합의 개수
        sum_sub = 0
        len_sub = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum_sub += A[j]
                len_sub += 1
        if len_sub == N and sum_sub == K:
            count += 1
    print('#%d %d'%(test_case, count))





