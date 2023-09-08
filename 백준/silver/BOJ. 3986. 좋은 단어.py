N = int(input())
word = [input() for _ in range(N)]
stack = []
ans = 0

for i in range(len(word)):
    for j in word[i]:
        if not stack:
            stack.append(j)
        else:
            if j == stack[-1]:
                stack.pop()
            else:
                stack.append(j)

    if len(stack) == 0:
        ans += 1
    stack.clear()

print(ans)

