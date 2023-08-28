# 내가 놓친 부분 => 최솟값을 구하는 프로그램
# min을 써야 한다
N = int(input())
street = list(input())
dp = [1e9] * (N) # 에너지 양 체크
dp[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if street[i] == "B" and street[j] == "O":
            dp[j] = min(dp[j], dp[i]+(j-i) * (j-i))
        elif street[i] == "O" and street[j] == "J":
            dp[j] = min(dp[j], dp[i]+(j-i) * (j-i))
        elif street[i] == "J" and street[j] == "B":
            dp[j] = min(dp[j], dp[i]+(j-i) * (j-i))

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[-1])

