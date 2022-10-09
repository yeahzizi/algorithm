#w,r,b가 차례대로 들어가는 모든 경우의 수(blank)와 문제의 입력값을 비교한다.
#blank와 입력값을 하나하나 비교해서 다를 때 1씩 카운트 한다.
#비교를 마친 카운트 값을 ans라는 빈 리스트에 append 하고, ans에서 제일 작은 값 출력
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    russia = [list(input()) for _ in range(N)]
    ans = []

    for i in range(1, N-1):
        for j in range(i+1, N):
            blank = [["W"] * M for _ in range(i)] + [["B"] * M for _ in range(i, j)] + [["R"] * M for _ in range(j, N)]
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if russia[r][c] != blank[r][c]:
                        cnt += 1
            ans.append(cnt)

    print(f'#{tc} {min(ans)}')
