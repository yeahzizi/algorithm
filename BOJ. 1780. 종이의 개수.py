N = int(input())
arr = [[0] * N for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

cnt = {-1:0, 0:0, 1:0}


