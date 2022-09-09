T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    pal = 0

    for i in range(int(A), int(B)+1):
        root = (i**(1/2))
        if str(root):
            if str(i) == str(i[::-1]):
                if str(root) == str(root[::-1]):

                    pal += 1

    print(pal)
