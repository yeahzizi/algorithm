T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    root = min(arr)
    arr.sort()
    heap = [[0, i] for i in range(N)]

    for i in range(N):
        heap[i][0] += arr[i]

    for i in range(N, -1, -1):
        




