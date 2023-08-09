N, K = map(int, input().split())
purse = []

for _ in range(N):
    purse.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    cnt += K // purse[i]
    K = K % purse[i]

print(cnt)
