N = int(input())
age = []

for n in range(N):
    i, j = input().split()
    age.append([int(i), j])

age.sort(key=lambda x: x[0])

for i in age:
    print(*i)