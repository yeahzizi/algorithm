from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x > 0: #x가 자연수이면 heap 리스트에 넣어준다.
        heappush(heap, (-x, x))
        #최대힙은 음수로 변환한 값을 같이 튜플로 넣어줘서,
        #음수 기준으로 정렬하고, 원래 값을 뽑아낸다.
    elif x == 0 and len(heap) == 0:
        print(0)
    elif x == 0 and len(heap) >= 1:
        print(heappop(heap)[1])
        #음수 기준으로 정렬된 튜플에서 원래 값만 출력한다.