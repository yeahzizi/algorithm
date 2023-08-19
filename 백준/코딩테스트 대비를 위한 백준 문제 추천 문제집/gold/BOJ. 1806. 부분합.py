import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = 0
num_sum = num[0]
length = 100001

while start < N and end < N:
    if num_sum < S:
        end += 1
        if end == N:
            break
        else:
            num_sum += num[end]

    else:
        length = min(length, end - start + 1)
        num_sum -= num[start]
        start += 1
        if start == N:
            break

if length == 100001:
    print(0)
else:
    print(length)