N = int(input())

for _ in range(N):
    quiz = input()
    check = False
    ans = 0
    num = 0
    for i in quiz:
        if i == "O" and check == False:
            ans += 1
            num += 1
            check = True
        elif i == "X":
            num = 0
            check = False
        elif i == "O" and check == True:
            ans += (num + 1)
            num += 1
            check = True

    print(ans)