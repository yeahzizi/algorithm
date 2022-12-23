while True:
    num = input()

    if num == "0":
        break

    pal = ""
    for i in range(len(num), -1):
        pal.join(num[i])
        print(num[i])

    if pal == num:
        print("yes")
    else:
        print("no")
