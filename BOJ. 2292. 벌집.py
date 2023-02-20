N = int(input())

bee = 1
cnt = 1
while N > bee:
    bee += cnt * 6
    cnt += 1

print(cnt)