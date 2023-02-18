def preorder(n): #전위순회
    if n: #0이 아니면
        ans.append(n)
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    V = int(input()) #정점 개수, 마지막 정점 번호
    arr = list(map(int, input().split()))
    E = V - 1 #간선 수

    #부모를 인덱스로 자식 번호 저장
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    #자식을 인덱스로 부모를 저장 (조상이나 루트 구할 때)
    par = [0] * (V+1)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0: #아직 자식이 없으면
            ch1[p] = c  #자식1로 저장
        else:
            ch2[p] = c
        par[c] = p

    ans = []
    preorder(1)
    print(f'#{tc}', *ans)