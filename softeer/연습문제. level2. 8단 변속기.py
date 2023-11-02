import sys
num = input()
arr = []

for i in num:
  if i != "_" and i != ' ':
    arr.append(int(i))

a_cnt, d_cnt = 0, 0
while True:
  now = arr.pop(0)
  if not arr:
    break
  elif now + 1 == arr[0]:
    a_cnt += 1
  elif now - 1 == arr[0]:
    d_cnt += 1

if a_cnt == 7:
  print("ascending")
elif d_cnt == 7:
  print("descending")
else:
  print("mixed")