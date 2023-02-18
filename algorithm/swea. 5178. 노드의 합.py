T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    V = N + 1
    tree = [[0, i] for i in range(V)]
    for i in range(M):
        num, value = input().split()
        for j in range(V):
            if int(num) == tree[j][1]:
                tree[j][0] += int(value)

    for i in range(V//2, -1, -1):
        if tree[i][0] == 0 and 0 < i <= N:
            tree[i][0] += tree[i*2][0]
            if (i * 2) + 1 > N:
                continue
            else:
                tree[i][0] += tree[(i * 2)+1][0]

    print(f'#{tc}', tree[L][0])








