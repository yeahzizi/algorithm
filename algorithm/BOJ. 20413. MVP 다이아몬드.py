N = int(input())
grade = list(map(int, input().split()))
MVP = list(input())
money = 0
monthly = [0] + [] * (N-1)

for i in range(N):
    if MVP[i] == "B":
        money += grade[0] - 1 - monthly[-1]
        monthly.append(grade[0]-1-monthly[-1])
    if MVP[i] == "S":
        money += grade[1]-1 - monthly[-1]
        monthly.append(grade[1]-1-monthly[-1])
    elif MVP[i] == "G":
        money += grade[2] - 1 - monthly[-1]
        monthly.append(grade[2]-1-monthly[-1])
    elif MVP[i] == "P":
        money += grade[3]-1 - monthly[-1]
        monthly.append(grade[3]-1-monthly[-1])
    elif MVP[i] == "D":
        money += grade[3]

print(money)


