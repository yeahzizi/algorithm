N = int(input())
ans = 1
cnt = 0

for i in range(1, N+1):
    ans = ans * i

ans = str(ans)

for i in range(len(ans)-1, -1, -1):
    if "0" not in ans:
        cnt = 0
        break
    if ans[i] == "0":
        cnt += 1
    elif ans[i] != "0":
        break

print(cnt)


