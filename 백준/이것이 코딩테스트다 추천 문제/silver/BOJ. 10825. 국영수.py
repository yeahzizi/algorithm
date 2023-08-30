N = int(input())
student = []

for _ in range(N):
    name, h, m, e = input().split()
    student.append((name, int(h), int(m), int(e)))

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in student:
    print(i[0])

