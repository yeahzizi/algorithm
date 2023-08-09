from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x > 0: #x가 자연수이면 heap 리스트에 원소를 넣어준다.
        heappush(heap, x)
        # heappush(넣을 곳, 넣을 원소)
    elif x == 0 and len(heap) == 0: #x가 0이면 출력해야 하는데, 길이도 0이면
        print(0) #0 출력
    elif x == 0 and len(heap) >= 1: #x가 0이고 출력할 내용이 있으면 출력
        print(heappop(heap))
        #heappop을 하면 최소값부터 출력된다.
