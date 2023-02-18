def inorder(n): #중위순회
    if n <= N:
        inorder(2*n)
        ans.append(tree_list[n])  # visit(n)
        inorder(2*n+1)

for tc in range(1, 11):
    N = int(input())
    tree_list = [""] * (N + 1)
    for i in range(1, N+1):
        list_input = input().split()
        tree_list[i] = list_input[1]

    ans = []
    inorder(1)
    print(f'#{tc} {"".join(ans)}')