import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deq = deque([])

for i in range(N):
    d = input().split()

    if d[0] == "push_front":
        deq.appendleft(int(d[1]))
    elif d[0] == "push_back":
        deq.append(int(d[1]))
    elif d[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif d[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif d[0] == "size":
        print(len(deq))
    elif d[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif d[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif d[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])


