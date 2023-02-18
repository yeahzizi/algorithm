T = int(input())
cnt = 0

for t in range(T):
    d = input()

    if len(d) == 5:
        cnt += 0

    elif len(d) == 3:
        cnt += 1

    elif len(d) == 4:
        if int(d[-2]) < 9 or (int(d[-2]) == 9 and int(d[-1]) == 0):
            cnt += 1

print(cnt)