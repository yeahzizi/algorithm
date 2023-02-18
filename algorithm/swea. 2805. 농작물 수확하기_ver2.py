#입력값 중 조건에 맞는 부분을 문자열로 받은 뒤,
#하나씩 int 값으로 바꿔서 더해준다.
for tc in range(1, int(input())+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    ans = ""
    result = 0

    for k in range(N//2+1):
        ans = farm[k][N//2-k:N//2+1+k]
        for i in ans:
            result += int(i)

    for k in range(1, N // 2 + 1):
        ans = farm[-k][N // 2 - (k-1):N // 2 + 1 + (k-1)]
        for i in ans:
            result += int(i)

    print(f'#{tc} {result}')