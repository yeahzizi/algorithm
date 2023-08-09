T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 10

    for i in range(0, N):  # k번만 굴리면 된다.
        maxIdx = i  # 구간의 맨 앞을 최소값으로 가정
        for j in range(i + 1, len(arr)):  # 실제 최소값 인덱스 찾기
            if arr[maxIdx] < arr[j]:
                maxIdx = j
        arr[maxIdx], arr[i] = arr[i], arr[maxIdx]  # 최소값을 구간 맨 앞으로

    for n in range(0, N, 2):
        cnt[n] = arr[int(n/2)]
        cnt[n+1] = arr[int(-(n/2)-1)]

    print(cnt)



