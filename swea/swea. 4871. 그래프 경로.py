T = int(input())
for test_case in range(1, T + 1):
    node, line = map(int, input().split())

    adj_matrix = [[0] * (node + 1) for _ in range(node + 1)]  # 인접행렬 기본틀 + 0번 포도알은 안씀

    for i in range(line):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1

    S, G = map(int, input().split())
    stack = [S]
    visited = []
    answer = 0

    while stack:  # 스택이 빌때까지 돌아라 라는 식을 줄거임
        current = stack.pop()  # pop(0)는 안할거임
        if current not in visited: #처음에는 visited가 비어 있음
            visited.append(current)
        if current == G:
            answer = 1
            break

        for destination in range(node + 1):
            if adj_matrix[current][destination] and destination not in visited:  # 이 값이 1인지 물어보는 것 and destination not in visited: #중복되지 않도록 not in visited 하기
                stack.append(destination)

    print(f'#{test_case} {answer}')