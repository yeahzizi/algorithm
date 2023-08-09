T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(n)]  # N*N 배열을 만든다.

    kill_bug = 0
    for i in range(n - m + 1):  # 스프레이를 뿌리는 공간을 이중 for문으로 설정한다.
        for j in range(n - m + 1):  # n-m+1로 범위를 설정해서 에러가 안나도록 한다.
            bug = 0
            for k in range(m):  # 죽인 파리 개수 구하기
                for b in range(m):
                    bug += space[k][b]

            if bug > kill_bug:  # 아래 두개의 for문에서 큰 값이 나오면 Kill_bug 값으로 갱신
                kill_bug = bug

    print(f'#{test_case} {kill_bug}')
