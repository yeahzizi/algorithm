N, K = map(int, input().split())
ans = [i for i in range(1, N+1)]
result = []

idx = 0
while ans:
    idx += K - 1
    if idx >= len(ans):
        idx %= len(ans)
    a = ans[idx]
    result.append(a)
    ans.remove(a)

print("<" +", ".join(map(str, result)) + ">")


