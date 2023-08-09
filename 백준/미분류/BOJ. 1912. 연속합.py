N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0] #dp의 첫번째 값은 입력 받은 리스트의 첫번째 값

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
    #dp[i] 값은 arr[i]값이거나,
    #그 전 dp 값(연속된 값)에 arr[i]를 더한 값이다.(둘 중 더 큰 값)

print(max(dp))