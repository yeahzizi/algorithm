N = int(input())
clap = ['3', '6', '9']
count = []

N = int(input())
clap = ['3', '6', '9']
count = []

for i in range(1, N+1):
    count.append(i)
    str_count = list(map(str, count))

for j in range(N):
    if str_count[j] in clap:
        str_count[j] = "-"

print(*str_count)






















