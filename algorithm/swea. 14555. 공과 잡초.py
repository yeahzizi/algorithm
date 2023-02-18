T = int(input())
for tc in range(1, T+1):
    S = input()
    cnt = 0

    for i in range(len(S)):
        if S[i:i+2] == "()":  #()가 붙어 있는 공이면 카운트
            cnt += 1

        if S[i] == "(" and S[i:i+2] != "()":  #공 앞부분이 있는데 완전하지 않으면 카운트
            cnt += 1

        if S[i] == ")" and S[i-1:i+1] != "()": #공 뒷부분이 있는데 완전하지 않으면 카운트
            cnt += 1

    print(f'#{tc} {cnt}')
