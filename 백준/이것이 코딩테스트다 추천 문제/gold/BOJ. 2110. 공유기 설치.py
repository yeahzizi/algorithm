#이분탐색
#전체 거리를 기준으로 함
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = []

for _ in range(N):
    array.append(int(input()))

array.sort()

start = 1 #최소거리
end = array[-1] - array[0] #최대거리

result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 1
    current = array[0]

    for i in range(N):
        if array[i] - current >= mid:
            cnt += 1
            current = array[i]

    if cnt >= C: # 공유기를 C보다 더 많이 둠
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1

print(result)