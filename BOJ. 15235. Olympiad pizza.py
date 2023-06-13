from collections import deque

N = int(input())
want = list(map(int, input().split()))
queue = deque()
cnt = [0] * N

for i in range(N):
    queue.append([i, want[i]])

get = 0
while queue:
    human, pizza = queue.popleft()
    get += 1
    cnt[human] = get

    if pizza == 1:
        pass
    else:
        queue.append([human, pizza-1])

print(*cnt)

