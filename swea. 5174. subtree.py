def f(n):  #global cnt 없이 방문한 정점 수를 리턴하는 함수
    if n == 0: #서브트리가 비어 있으면,
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    line = list(map(int, input().split()))
    V = E +1

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    tree_list = [0] * (V + 1)
    for i in range(E):
        p, c = line[i*2], line[i*2+1]
        if ch1[p] == 0:  # 아직 자식이 없으면
            ch1[p] = c  # 자식1로 저장
        else:
            ch2[p] = c
        tree_list[c] = p

    print(f'#{tc}', f(N))





