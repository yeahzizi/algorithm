T = int(input())
for tc in range(1, T+1):
    S = input()
    N = len(S) * 5 - (len(S)-1)  #세로의 길이를 N으로 정리
    diamond = [["."] * N for _ in range(5)]
    ans = ""

    for i in range(5):
        for j in range(N):
            for n in range(N//4):  #첫번째와 마지막줄 #의 인덱스를 구하기 위한 for문
                if i == 0 and j == (2 + (n * 4)):
                    diamond[i][j] = "#"
                if i == 1 and j % 2 == 1:
                    diamond[i][j] = "#"
                if i == 2 and j % 2 == 0:
                    diamond[i][j] = "#"  #일단 입력받은 문자열 대신 #을 넣음
                if i == 3 and j % 2 == 1:
                    diamond[i][j] = "#"
                if i == 4 and j == (2 + (n * 4)):
                    diamond[i][j] = "#"


    for j in range(N):
        for n in range(1, (N // 4)+1):
            if j == (2 + ((n-1)*4)):
                diamond[2][j] = S[n-1]

    for i in range(5):
        ans = "".join(diamond[i])
        print(ans)







