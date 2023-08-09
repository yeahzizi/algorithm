T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N % 2 == 0:
        print(f'#{tc} Alice')
        continue
    elif N % 2 == 1:
        print(f'#{tc} Bob')
        continue


