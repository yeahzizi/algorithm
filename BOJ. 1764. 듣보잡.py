N, M = map(int, input().split())
name_dict = {}

for i in range(N):
    name = input()
    name_dict[name] = i+1

ans = []
for _ in range(N+1, N+M):
    name = input()
    if name in name_dict:
        ans.append(name)

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])