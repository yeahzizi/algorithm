def inorder(n):
    global num
    if n <= (2**K)-1:
        inorder(2*n)
        tree[num][0] = n
        num += 1
        inorder(2*n+1)

K = int(input())
tree = [[0, i] for i in list(map(int, input().split()))]
num = 0

inorder(1)
tree.sort()

real_tree = [i[1] for i in tree]
ans = 0

for i in range(len(real_tree)):
    print(*real_tree[ans:ans*2+1])
    ans += 2**i




