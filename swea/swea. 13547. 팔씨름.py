T = int(input())
for tc in range(1, T+1):
    x_cnt = 0

    for i in input():
        if i == "x":   #x의 개수를 카운트한다.
            x_cnt += 1

    if x_cnt > 15 // 2: #15번의 절반 이상인 8번 이상 x라면 NO를 출력, 아니면 YES
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')




