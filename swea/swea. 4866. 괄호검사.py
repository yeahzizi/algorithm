T = int(input())
for test_case in range(1, T + 1):

    bracket = input()
    stack = []
    br_dict = {")":"(", "}":"{"} #괄호끼리 짝을 지어준다.

    for i in bracket:
        if i == "(" or i == "{":
            stack.append(i)

        elif i == ")" or i == "}":
            if not stack:  # stack이 비어 있음 stack == [] 와 같은데 깔끔
                stack.append(i)
                break
            else:
                if br_dict.get(i) == stack[-1]: #i의 짝이 stack 맨 아래와 같다면 pop 한다.
                    stack.pop()
                else:
                    stack.append(i)
                    break

    if not stack:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)