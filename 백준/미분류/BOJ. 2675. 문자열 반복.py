T = int(input())

for _ in range(T):
    n, word = input().split()
    n = int(n)
    ans = []
    for i in word:
        a = n
        while n > 0 and a > 0:
            ans.append(i)
            a -= 1


    print("".join(ans))

