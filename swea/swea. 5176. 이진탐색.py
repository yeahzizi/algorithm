def inorder(n):  # 중위순회
    global num
    if n <= E:
        inorder(2 * n)
        tree[num+1][0] = n
        num += 1
        inorder(2 * n + 1)

T = int(input())
for tc in range(1, T+1):
    E = int(input())
    tree = [[0, i] for i in range(E+1)]
    num = 0

    inorder(1)

    print(tree)

    root = 0
    result = 0
    for i in range(len(tree)):
        if tree[i][0] == 1:
            root = tree[i][1]
        if tree[i][0] == E//2:
            result = tree[i][1]

    print(f'#{tc} {root} {result}')