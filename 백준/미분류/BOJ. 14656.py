N = int(input())
line = list(map(int, input().split()))
punch = 0

for i in range(1, N+1):
    if i != line[i-1]:
        punch += 1

print(punch)


