space = [[0] * 10 for _ in range(10)]
N, M = list(map(int, input().split()))
T = int(input())
width = [0] * T
height = [0] * T

for t in range(T):
    x, y = list(map(int, input().split()))
    if x == 0 and width[t] <= M-y:
        width[t] = M-y
    if x == 1 and height[t] <= N-y:
        height = N-y

print(width * height)






