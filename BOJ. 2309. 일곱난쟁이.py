#부분집합 합으로 구현
short = [int(input()) for _ in range(1, 10)] #입력 받은 값을 하나의 리스트로 만듦
real_short = []

for i in range(1 << len(short)):  # 0부터 2^n - 1 만큼 돌려줌 > 1>>n은 부분 집합의 개수
    sum_short = []
    for j in range(len(short)): #i의 j번째 비트가 1이면 j번째 원소 출력
        if i & (1 << j):
            sum_short.append(short[j])

    if len(sum_short) == 7 and sum(sum_short) == 100:
        real_short = sorted(sum_short) #sorted를 사용해 새로운 리스트로 반환
        break

for real in real_short:
    print(real)








