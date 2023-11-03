# 빡구현일때, 코드 주의해서 짜기!!!

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
name = []
for _ in range(n):
    a = input().strip()
    name.append([a, [0] * 9])

for _ in range(m):
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    for n, dp in name:
        if n == a:
            for i in range(b - 9, c - 9):
                dp[i] += 1

name.sort(key=lambda x: x[0])

for room, dp in name:
    print(f'Room {room}:')
    if 0 not in dp:
        print('Not available')
    else:
        cnt = []
        ans = []
        for i in range(9):
            if dp[i] == 0:
                cnt.append(i + 9)
                cnt.append(i + 10)
            else:
                if cnt:
                    ans.append(cnt)
                    cnt = []
        if cnt:
            ans.append(cnt)

        if ans:
            print(f'{len(ans)} available:')
            for i in ans:
                print(f'{i[0]:02d}-{i[-1]:02d}')

    if room != name[-1][0]:
        print("-----")