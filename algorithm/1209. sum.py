for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    #배열이 100 * 100이니 100번 입력 받음(range가 100)

    #초기 Max값 설정
    maxV = 0 #max = float('-inf') 이면 음수로 초기값 설정한 것
    for i in range(100):
        maxV += arr[0][i] #초기 값을 첫 행의 합으로 둔다.


    # 가로 합 구하고 maxV 값 갱신
    for i in range(1, 100):  # 각 행에 접근
        width_sum = 0  # 가로 합을 0으로 둠, 밖에 for문에 영향 받지 않도록 안에 적어줌
        for j in range(100):  # i행의 j열에 접근
            width_sum += arr[i][j]
        if width_sum > maxV: #가로 합이 maxV보다 크면 maxV로 갱신함
            maxV = width_sum

    # 세로 합 구하고 maxV 값 갱신
    for i in range(100): # 각 열에 접근
        hight_sum = 0  # 세로 합을 0으로 둠
        for j in range(100):  # j행의 i열에 접근
            hight_sum += arr[j][i]
        if hight_sum > maxV:
            maxV = hight_sum

    #왼쪽에서 시작하는 대각선 합 구하고 maxV 값 갱신
    left_start = 0
    for i in range(100):
        left_start += arr[i][i]  #인덱스가 같은 값이 대각선이니 서로 더한다.
    if left_start > maxV:
        maxV = left_start

    #오른쪽에서 시작하는 대각선 합 구하고 maxV 값 갱신
    right_start = 0
    for i in range(100):
        right_start += arr[i][99-i] #오른쪽에서 시작하는 대각선 인덱스 합은 99이다.
    if right_start > maxV:
        maxV = right_start


    print(f'#{test_case} {maxV}')

