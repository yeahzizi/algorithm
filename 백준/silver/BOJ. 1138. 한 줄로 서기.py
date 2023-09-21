N = int(input())
row = list(map(int, input().split()))
height = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == row[i] and height[j] == 0:
            height[j] = i+1
            break
        elif height[j] == 0:
            cnt += 1

print(*height)