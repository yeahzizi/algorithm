tem_list = []
while True:
    tem = float(input())
    if tem == 999:
        break
    else:
        tem_list.append(tem)

change = 0
for i in range(len(tem_list)-1):
    change = tem_list[i+1] - tem_list[i]
    print(f'{change:.2f}')





