# 벽을 칠수도 있고, 인덱스 컨트롤을 할 수도 있다.
# dfs의 풀이방법이 스택과 재귀
#

def maze_call(r, c):
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                r, c = i, j
    Q = [[r, c]] # 기본시작점 setting
    visited = [] # 방문하는 곳들을 저장할 빈 list를 생성
    while Q: # Q의 원소가 있을 동안에
        [r, c] = Q.pop() # 시작점을 뽑아내고
        visited.append([r, c]) # 방문한 곳에 담고
        for i in range(4): # 방향전환
            r1 = r + dr[i]
            c1 = c + dc[i]

            if 0 <= r1 < N and 0 <= c1 < N: # index error를 방지하는 조건
                if not maze[r1][c1] and [r1, c1] not in visited: # maze[r1][c1] == 0일때
                    Q.append([r1, c1]) #
                if maze[r1][c1] == 3:
                    ans = 1
                    break
    return ans


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dr = [0, 1, 0, -1]  # 우 -> 하 -> 좌 -> 상이 한 사이클이라고 생각
    dc = [1, 0, -1, 0]  # 우하좌상
    print(f'#{test_case} {maze_call(0,0)}')

    maze_call(0, 0)


"""
#교수님 코드
T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)] #list 안에 input을 넣어야 쪼개짐
    visited = set() #중복 없앰
    answer = 0

    initial_r = None
    initial_c = None
    for i in range(N):
        flag = False

        for j in range(N):
            if maze[i][j] == 2:
                initial_r = i
                initial_c = j
                flag = True
                break

        if flag:
            break

        stack = [(initial_r, initial_c)]

        while stack:
            r, c = stack.pop()
            visited.add((r, c))

            if maze[r][c] == 3:
                answer = 1
                break

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 < nr <= N or 0 < nc <= N:
                    continue

                if maze[nr][nc] == 1 or (nr, nc) in visited:
                    continue

                stack.append((nr, nc))

        print(f'{tc} {answer}')
"""