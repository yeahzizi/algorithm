A = input()
cnt = A.count('a')

A = A + A
ans = int(1e9)
for i in range(len(A) - cnt):
    ans = min(ans, A[i:i+cnt].count('b'))

print(ans)

