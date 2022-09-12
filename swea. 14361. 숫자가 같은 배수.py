#재귀수열
def perm(depth):
    global result
    if depth == len(N): #1배수를 제외한 배수일 때 possible 출력
        if not(int(''.join(ans)) % int(N)) and int(''.join(ans)) != int(N):
            result = "possible"
            return

    for i in range(len(N)):
        if not check[i]:
            check[i] = 1
            ans[depth] = N[i]
            perm(depth+1)
            check[i] = 0 #돌려주기

T = int(input())
for tc in range(1, T + 1):
    N = input()
    check = [0]*len(N) #뽑을지 말지 결정
    ans = [0]*len(N)
    result = "impossible"
    perm(0)
    print(f'#{tc} {result}')














