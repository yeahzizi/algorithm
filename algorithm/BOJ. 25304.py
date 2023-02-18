X = int(input())
T = int(input())
sum = 0
for tc in range(1, T+1):
    a, b = map(int, input().split())

    sum += a * b

if X == sum:
    print("Yes")
else:
    print("No")