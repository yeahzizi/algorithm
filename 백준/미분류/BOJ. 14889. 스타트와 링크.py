import sys
N = int(sys.stdin.readline())
startlink = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [False] * (N+1)
result = 10000000

def dfs(depth, idx):
    global result
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visit[i] and visit[j]:
                    start += (startlink[i][j] + startlink[j][i])
                elif not visit[i] and visit[j]:
                    link += (startlink[i][j] + startlink[i][j])

        result = min(result, abs(start - link))  # 최솟값을 결과값에 대입
    for i in range(idx, N):
        if not visit[i]:  # 만약 방문을 안했다면
            visit[i] = True  # 방문으로 처리
            dfs(depth + 1, i + 1)  # 재귀를 돈다
            visit[i] = False  # 방문 완료 처리

dfs(0, 0)
print(result)