def dfs(n):
    if n not in visited:  # 우선 visited 없으면 넣어줌
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)  # 다음 재귀 깊이로 이동




for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

visited = []  # 궤적 기록용

dfs(1)  # 1번 포도알부터 시작!

print('이동경로:', *visited)





R, C = list(map(int, input().split()))
field = [list(input().split()) for _ in range(C)]

sheep = []


for i in range(R):
    for j in range(C):
        print()
for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

Q = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while Q:  # 큐가 빌때까지 돌아라!
    current = Q.pop(0)  # 우선 큐에서 현재 위치 "앞에서부터" 뽑고,
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in range(V+1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
            Q.append(destination) # 다음 갈 곳으로 큐에 저장

print('이동경로:', *visited)