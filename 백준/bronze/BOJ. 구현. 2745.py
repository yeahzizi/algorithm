N, B = input().split()

N = N[::-1]
B = int(B)
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0

for i, char in enumerate(N):
    idx = number.index(char)
    ans += (idx * (B**(i)))

print(ans)