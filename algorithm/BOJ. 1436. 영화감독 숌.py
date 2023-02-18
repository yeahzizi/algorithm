N = int(input())
death = "666"
cnt = 0

for i in range(666*10000):
    if death in str(i):
        cnt += 1
        if cnt == N:
            print(i)



