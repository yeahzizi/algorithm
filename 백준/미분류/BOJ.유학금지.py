voca = input()
uni = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
voca_list = list(voca)
new_voca = []

for v in range(len(voca_list)):
    if voca_list[v] not in uni:
        new_voca.append(voca_list[v])


print("".join(new_voca))











