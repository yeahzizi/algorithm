N = int(input())
consult = {}

for i in range(N):
    n, m = map(int, input().split())
    consult[i] = (n, m)

print(consult)