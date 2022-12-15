N = int(input())
dp = [0] * 301
stairs = [0] * 301
#계단의 리스트를 최대인 300개 초과로 설정해야 두번째 for문에서 인덱스 에러가 나지 않는다.
for i in range(N):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1]+stairs[2])
#여기서 주의 마지막 계단은 꼭 밟아야 한다!!

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[N-1])
