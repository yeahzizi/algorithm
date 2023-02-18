T = int(input())
for tc in range(1, T+1):
    A, B = list(input().split())
    count = 0

    for i in range(int(A), int(B)+1):
        root = i**(1/2)
        if root == round(root): #그냥 root가 반올림한 root가 같다면 = root가 자연수라면
            root = str(int(root))
            pal_root = root[::-1] #자연수인 root만 뒤집음
            if root == pal_root: #root와 뒤집은 root가 같을 때만,
                i = str(i)
                pal = i[::-1]
                if i == pal: #i와 뒤집은 i가 같은 지 확인
                    count += 1

    print(f'#{tc} {count}')
