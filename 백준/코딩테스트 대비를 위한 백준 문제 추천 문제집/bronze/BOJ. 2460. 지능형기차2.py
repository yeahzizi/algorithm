num = []
people = 0
for _ in range(10):
    n, m = map(int, input().split())
    people -= n
    people += m
    num.append(people)

print(max(num))