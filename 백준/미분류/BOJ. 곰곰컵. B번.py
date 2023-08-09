T = int(input())
dance = ['ChongChong']

for t in range(T):
    i, j = input().split()

    if i in dance:
        dance.append(j)

    if j in dance:
        dance.append(i)

print(len(set(dance)))


