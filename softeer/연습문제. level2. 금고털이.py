import sys

wei, kind = input().split(" ")
bag = []
for _ in range(int(kind)):
    jew, w = input().split(" ")
    a = int(jew)
    bag.append([a, int(w)])

bag.sort(key=lambda x: x[1], reverse=True)

ans = 0
wei = int(wei)
for i, j in bag:
    if wei >= i:
        ans += (i * j)
        wei -= i
    else:
        ans += (wei * j)
        break

print(ans)



