#25분
N = int(input())
switch = list(map(int, input().split()))
student = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    student.append([n, m])

for s, num in student:
    if s == 1:
        for change in range(len(switch)):
            if (change + 1) % num == 0:

                if switch[change] == 1:
                    switch[change] = 0
                else:
                    switch[change] = 1

    if s == 2:
        left, right = num-1, num-1
        if switch[left] == 1:
            switch[left] = 0
        else:
            switch[left] = 1
        while True:
            left, right = left-1, right+1
            if 0 <= left < len(switch) and 0 <= right < len(switch):
                if switch[left] == switch[right]:
                    if switch[left] == 1:
                        switch[left], switch[right] = 0, 0
                    else:
                        switch[left], switch[right] = 1, 1
                else:
                    break
            else:
                break

for i in range(len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()

