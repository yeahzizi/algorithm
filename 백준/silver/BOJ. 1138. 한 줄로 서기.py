N = int(input())
row = list(map(int, input().split()))
height = [0] * N
height[row[0]] = 1

print(height)