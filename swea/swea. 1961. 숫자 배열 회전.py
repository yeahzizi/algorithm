T = int(input())
for tc in range(T):
    N = int(input())
    square = [list(map(str, input().split())) for _ in range(N)] #str로 받아야 join을 쓸 수 있음
    square_zip = list(map(list, zip(*square))) #zip한다.
    answer = []

    square90 = [i[::-1] for i in square_zip] #[[7, 4, 1], [8, 5, 2], [9, 6, 3]] #뒤집는 식 외우기
    square180 = [j[::-1] for j in square[::-1]] #[9, 8, 7], [6, 5, 4], [3, 2, 1]
    square270 = square_zip[::-1] #[3, 6, 9], [2, 5, 8], [1, 4, 7]

    print(f'#{tc+1}')
    for i in range(N):
        print("".join(square90[i]), "".join(square180[i]),"".join(square270[i]))





