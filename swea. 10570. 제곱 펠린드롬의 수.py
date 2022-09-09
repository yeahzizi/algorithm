T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    count = 0

    for i in range(int(A), int(B)+1):
        root = i**(1/2)
        if root == round(root):
            root = str(int(root))
            pal_root = root[::-1]
            if root == pal_root:
                i = str(i)
                pal = i[::-1]
                if i == pal:
                    count += 1

    print(f'#{tc} {count}')
