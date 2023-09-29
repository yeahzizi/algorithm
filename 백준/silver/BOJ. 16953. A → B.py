from collections import deque
A, B = map(int, input().split())

ans = 1
q = deque()
q.append(B)

while True:
    num = q.popleft()
    if num == A:
        print(ans)
        break
    elif num % 2 == 0:
        num = num // 2
        q.append(num)
        ans += 1
    elif num > 1 and str(num)[-1] == "1":
        n = len(str(num))
        num = str(num)[:-1]
        q.append(int(num))
        ans += 1
    else:
        print(-1)
        break

