from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heappush(heap, x)
    elif x == 0 and len(heap) == 0:
        print(0)
    elif x == 0 and len(heap) >= 1:
        print(heappop(heap))
