import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 0
cnt, ans = 0, 0
check = [0] * 100001

while end < N:
    if check[num[end]] < K:
        check[num[end]] += 1
        cnt += 1
        end += 1
    else:
        check[num[start]] -= 1
        cnt -= 1
        start += 1
    ans = max(ans, cnt)
        
        
print(ans)



