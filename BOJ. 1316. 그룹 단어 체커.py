N = int(input())
alp = [input() for i in range(N)]
ans = [] * N

cnt = N

for i in range(N):
    for j in alp[i]:
        ans.append(j)
    ans.append(1)

for i in range(len(ans)-2):
    if ans[i] == ans[i+1]:
        ans.remove(ans[i])

result = []
for i in ans:
    if i in result:
        cnt -= 1
        result.append(i)
    elif i not in result:
        result.append(i)
    elif i == 1:
        result = []


print(cnt)

