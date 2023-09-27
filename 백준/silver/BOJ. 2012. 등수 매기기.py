import sys
input = sys.stdin.readline

N = int(input())
rank = [int(input()) for _ in range(N)]
rank.sort()

ans = 0
for i in range(N):
    ans += abs(rank[i] - (i+1))
print(ans)