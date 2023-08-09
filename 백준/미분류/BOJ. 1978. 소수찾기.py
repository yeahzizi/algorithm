N = int(input())
num = list(map(int, input().split()))
cnt = 0

for n in num:
    err = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                err += 1
        if err == 0:
            cnt += 1

print(cnt)



