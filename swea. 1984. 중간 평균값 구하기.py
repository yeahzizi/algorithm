T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))

    num.remove(max(num)) #리스트에서 max 값과 min 값을 뺀다.
    num.remove(min(num))

    avg = round(sum(num) / len(num)) #평균 구하고 round로 반올림

    print(f'#{tc} {avg}')