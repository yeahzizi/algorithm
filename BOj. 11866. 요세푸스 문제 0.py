N, K = map(int, input().split())
ans = []

for i in range(1, N+1):
    ans.append(i)

ans = ans * N
remove_set = []
visited = []
while ans:
    for i in range(1, len(ans), 3):
        visited.append(ans[i + 1])
        remove_set.append(ans[i + 1])
    ans = [i for i in ans if i not in remove_set]



print(visited)


