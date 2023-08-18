giho = list(input())
stack = []
cnt = 1 #ans에 합산할 변수
ans = 0 #최종정답

for i in range(len(giho)):
    if giho[i] == "(":
        cnt *= 2
        stack.append(giho[i])

    elif giho[i] == "[":
        cnt *= 3
        stack.append(giho[i])

    elif giho[i] == ")":
        if not stack or stack[-1] != "(":
            ans = 0
            break
        if giho[i-1] == "(":
            ans += cnt
        stack.pop()
        cnt //= 2

    elif giho[i] == "]":
        if not stack or stack[-1] != "[":
            ans = 0
            break
        if giho[i-1] == "[":
            ans += cnt
        stack.pop()
        cnt //= 3

if len(stack) > 0:
    print(0)
elif len(stack) == 0:
    print(ans)


