int_count = map(int, input().split())
count = []
for i in int_count:
    if i > 0:
        count.append(i)
print(len(count))