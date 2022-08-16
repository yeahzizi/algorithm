T = int(input())
for test_case in range(1, T + 1):
    N = input()
    M = input()

    count = M.replace(N, "*")

    if "*" in count:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)