N = int(input())


for i in range(N):
    vps = "NO"
    stack = []
    cnt = 0
    xy = list(input())
    for j in range(len(xy)):
        if xy[j] == "(":
            stack.append("(")
            cnt += 1
        else:
            if len(stack) >= 1 and stack[-1] == "(":
                stack.pop()
                cnt += 1
            else:
                stack.append(")")

    if cnt == len(xy) and len(stack) == 0:
        vps = "YES"

    print(vps)





