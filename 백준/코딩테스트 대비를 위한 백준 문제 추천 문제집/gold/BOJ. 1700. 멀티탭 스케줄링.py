import sys

input = sys.stdin.readline
N, K = map(int, input().split())
electronics = list(map(int, input().split()))
plug = [0] * N  # 멀티탭에 꽂힌 전기용품을 check 할 거임
ans = 0

while electronics:
    electronic = electronics[0]
    # 멀티탭에 빈 자리가 있고 + (주의)이전에 꽂힌 게 없을 때
    if 0 in plug and electronic not in plug:
        plug[plug.index(0)] = electronic
        electronics.remove(electronic)

    # 빈자리는 없는 데 이전에 꽂힌게 아직도 있을 때
    elif electronic in plug:
        electronics.remove(electronic)

    # 빈자리도 없고 꽂힌 것도 없을 때
    # 1) 다음에 사용 안 할 플러그를 뽑아버리자
    # 2) 1의 경우가 없으면 가장 나중에 쓸 플러그부터 뽑자
    else:
        for i in plug:
            if i not in electronics:
                plug[plug.index(i)] = electronic
                electronics.remove(electronic)
                ans += 1
                break

        else:
            find = []
            for j in electronics:
                if j in plug and j not in find:
                    find.append(j)

            last = find[-1]
            plug[plug.index(last)] = electronic
            electronics.remove(electronic)
            ans += 1

print(ans)




