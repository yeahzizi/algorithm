for tc in range(10):
    N = int(input())
    tree = [0] * (N + 1)
    result = []
    for i in range(N):
        arr = input().split()
        if len(arr) == 4:
            result.append(arr)
        else:
            tree[int(arr[0])] = int(arr[1])
    print(tree, result)
    for i in range(len(result)-1, -1, -1):
        if result[i][1] == "+":
            tree[int(result[i][0])] = tree[int(result[i][2])] + tree[int(result[i][3])]
        if result[i][1] == "-":
            tree[int(result[i][0])] = tree[int(result[i][2])] - tree[int(result[i][3])]
        if result[i][1] == "*":
            tree[int(result[i][0])] = tree[int(result[i][2])] * tree[int(result[i][3])]
        if result[i][1] == "/":
            tree[int(result[i][0])] = round(tree[int(result[i][2])] / tree[int(result[i][3])])

    print(f'#{tc+1} {tree[1]}')







