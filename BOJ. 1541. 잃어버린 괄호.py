num = input()
num_split = num.split("-")
expression = []

for i in num_split:
    ans = 0
    plus = i.split("+")
    for j in plus:
        ans += int(j)
    expression.append(ans)

answer = expression[0]
for i in range(1, len(expression)):
    answer -= expression[i]

print(answer)


