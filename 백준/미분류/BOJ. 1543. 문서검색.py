voca = input()
find = input()
cnt = 0
idx = 0

for i in range(len(voca)):
    if idx > i:
        continue
    if voca[i:len(find)+i] == find:
        cnt += 1
        idx = i + len(find)

print(cnt)



