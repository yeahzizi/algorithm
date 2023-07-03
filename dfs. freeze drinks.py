# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

# 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph[i] = list(map(int, input()))

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우 모두 재귀적으로 호출
        # 결과적으로 0이 하나만 존재해도 return True로 result +1 가능
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # 상하좌우 모두 호출하고 끝내면 '성공'처리(이 코드가 없으면 다음 줄에서 실패로 넘어감)
        return True
    # 주어진 범위를 벗어나지도 않고 graph[x][y] == 0도 아닌 경우 '실패'처리
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

# 참고 블로그: https://hgk5722.tistory.com/8