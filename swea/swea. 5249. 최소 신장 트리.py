T = int(input())

def make_set(x):
    parent[x] = x

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    parent[find_set(y)] = find_set(x)  #여기서 한번 더 find_set으로


for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range (E)]
    edges.sort(key=lambda x: x[2])
    parent = [0] * (V+1)

    for i in range(V+1):
        make_set(i)

    answer = 0
    cnt = 0

    for x, y, w in edges:
        if find_set(x) != find_set(y):
            union(x, y)
            answer += w
            cnt += 1

        if cnt == V:
            break

    print('#{} {}'.format(tc, answer))




