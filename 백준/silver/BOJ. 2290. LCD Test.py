S, N = map(int, input().split())
str_N = str(N)
monitor = []

def lcd(x):
    sero = 2*S+3
    graph = [[""] * (S + 2) for _ in range(sero)]
    for i in range(S+2):
        for j in range(sero):
            if x == 1:
                if i == S+1 and j != 0 and j != sero and j != sero//2+1:
                    graph[j][i] = "|"
            if x == 2:
                if S-1 <= i <= S and (j != 0 or j != sero or j != sero//2+1):
                    graph[j][i] = "-"
                elif i == S-2 and (sero//2+1 < j < sero):
                    graph[j][i] = "|"


    return graph


for i in str_N:
    if i == "1":
        monitor.append(lcd(1))
    elif i == "2":
        monitor.append(lcd(2))
    elif i == "3":
        monitor.append(lcd(3))
    elif i == "4":
        monitor.append(lcd(4))
    elif i == "5":
        monitor.append(lcd(5))
    elif i == "6":
        monitor.append(lcd(6))
    elif i == "7":
        monitor.append(lcd(7))
    elif i == "8":
        monitor.append(lcd(8))
    elif i == "9":
        monitor.append(lcd(9))

print(monitor)


