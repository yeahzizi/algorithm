N = int(input())
number = input().split()
line = []

for i in range(N): #뽑은 숫자만큼 앞으로 간 뒤 insert 한다.
    line.insert(i-int(number[i]), i+1)

print(*line)





