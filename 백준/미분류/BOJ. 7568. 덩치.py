N = int(input())
dung = []
for _ in range(N):
    x, y = map(int, input().split())
    dung.append((x, y))

for i in dung:
    rank = 1
    for j in dung:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=" ")

