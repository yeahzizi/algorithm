from itertools import combinations

N = int(input())

ans = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        ans.append(int("".join(map(str, num))))

ans.sort()
if N >= len(ans):
    print(-1)
else:
    print(ans[N])