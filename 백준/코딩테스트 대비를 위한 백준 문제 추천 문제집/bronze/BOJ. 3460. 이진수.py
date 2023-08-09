# 처음에 메모리 초과가 떴다...
# 메모리 초과 코드
# 어느 부분을 합칠 수 있을 지 고민해서 풀어야 한다
T = int(input())

for _ in range(T):
    N = int(input())

    num = []
    while True:
        num.append(N % 2)
        N = N // 2
        if N == 1:
            num.append(N)
            break

    for i in range(len(num)):
        if num[i] == 1:
            print(i, end = ' ')

# 정석? 풀이
T = int(input())

for _ in range(T):
    N = int(input())

    i = 0
    while N > 0:
        if N % 2 == 1:
            print(i, end = ' ')
        N = N // 2
        i += 1
