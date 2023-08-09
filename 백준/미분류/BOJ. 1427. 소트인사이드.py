N = list(input())
num = []

for i in range(len(N)):
    num.append(int(N[i]))
    #입력받은 값을 쪼개서 정수로 리스트에 저장

num.sort(reverse=True) #저장한 리스트를 큰 수부터 정렬
for i in num:
    print(i, end='')
    #리스트에 저장 된 수를 세로가 아닌 가로로 붙여서 출력


