num = list(map(int, input().split()))
pal = []

for i in range(2):
    num[i] = str(num[i])

for i in range(2):
    ans = ""
    cnt = 0
    for j in range(len(num), -1, -1):
        ans += str(num[i][j])
        cnt += 1
        if cnt == 3:
            pal.append(ans)

print(max(pal))









