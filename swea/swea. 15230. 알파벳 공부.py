# alp와 input 인덱스의 값이 같으면 +1 다르면 바로 break로 for문 빠져나오기
# 안빠져나오면 그 다음값도 계속 카운트 된다.
T = int(input())
for tc in range(1, T+1):
    S = input()
    alp = ["abcdefghijklmnopqrstuvwxyz"]
    ans = 0

    for i in range(len(S)):
        if alp[0][i] == S[i]:
            ans += 1
        else:
            break

    print(f'#{tc} {ans}')