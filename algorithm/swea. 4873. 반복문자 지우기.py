T = int(input())
for test_case in range(1, T + 1):
    s = list(map(str, input())) #알파벳 하나씩 입력받기
    stack = [0]
    top = 0

    for i in s:
        if i != stack[top]: #제일 늦게 넣은 문자와 지금 넣은 문자가 다르면,
            stack.append(i) #지금 넣은 문자를 stack에 쌓는다.
            top += 1

        else:
            stack = stack[:-1] #맨 오른쪽 값을 제외하고 출력
            top -= 1

    print(f'#{test_case} {len(stack)-1}')




"""
    while True:
        button = 0
        for i in range(len(s)-2):
            if s[i] == s[i+1]:
                s.remove(s[i])
                s.remove(s[i])
                button = 1
                break
        if button == 0:
            break

    print(s)
"""