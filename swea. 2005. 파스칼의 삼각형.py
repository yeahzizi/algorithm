T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pascal = [[1] * i for i in range(1, N+1)] # 요소가 1,2,3,4개 리스트로 출력

    for m in range(N):
        for n in range(len(pascal[m])-1):
            pascal[0][0] = 1
            pascal[m][0] = 1
            pascal[m][m] = 1
            if m >= 2 and n >= 1:
                pascal[m][n] = pascal[m-1][n-1] + pascal[m-1][n]

    print("#%d"%test_case)
    for k in pascal:
        print(*k)
