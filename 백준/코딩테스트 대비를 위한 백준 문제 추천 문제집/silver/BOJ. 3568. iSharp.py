variable = input()
variable_list = variable.split(' ')
basic = variable_list[0]
variable_list.remove(basic)

stack = []
for i in variable_list:
    i = i.replace(",", "")
    i = i.replace(";", "")
    word = ""
    for j in reversed(range(len(i))):
        if not i[j].isalpha():

            if i[j] == "]":
                word += "".join("[")
            elif i[j] == "[":
                word += "".join("]")
            else:
                word += "".join(i[j])
    stack.append(word)

    ans = basic + word
    print(ans, end=" ")

    for al in i:
        if al.isalpha():
            print(al, end='')

    print(";")




