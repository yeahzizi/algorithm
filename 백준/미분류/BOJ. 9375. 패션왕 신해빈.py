T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        cloth, typ = input().split()
        if typ in clothes.keys():
            clothes[typ].append(cloth)
        else:
            clothes[typ] = [cloth]

    ans = 1
    for i in clothes.keys():
        ans += ans * len(clothes[i])

    print(ans-1)
