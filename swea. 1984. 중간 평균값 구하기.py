T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))

    num.remove(max(num))
    num.remove(min(num))

    avg = round(sum(num) / len(num))

    print(f'#{tc} {avg}')