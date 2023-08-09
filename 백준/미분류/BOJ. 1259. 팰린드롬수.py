while True:
    num = input()
    if num == "0":
        break

    pal = ""
    for i in range(1, len(num)+1):
        pal += num[-i]

    if num == pal:
        print("yes")
    else:
        print("no")
