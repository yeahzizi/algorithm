from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
for i in combinations(range(0, N), N//2):
    team_a = list(i)
    team_b = [i for i in range(0, N) if i not in team_a]

    a = 0
    b = 0
    for j in range(len(team_a)):
        for k in range(j+1, len(team_a)):
            a += arr[team_a[j]][team_a[k]] + arr[team_a[k]][team_a[j]]
            b += arr[team_b[k]][team_b[j]] + arr[team_b[j]][team_b[k]]

    ans = min(ans, abs(a-b))

print(ans)


