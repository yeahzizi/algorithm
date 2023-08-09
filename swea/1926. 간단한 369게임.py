N = int(input())
clap = ['3', '6', '9']
count = []

for i in range(1, N+1): # 1~N까지 count라는 리스트에 넣은 뒤 문자열로 만든다.
    count.append(i)
    str_count = list(map(str, count))

for j in range(N): #슬라이싱을 이용하여 clap이 str_count 안에 있는 지 비교한다.
    if str_count[j] in clap: #테스트 케이스는 총 100까지 이므로 99까지 해당하는 조건을 만듦
        str_count[j] = "-"
    elif (str_count[j][1:] in clap) and (str_count[j][:1] in clap):
        str_count[j] = "--" #십의자리수, 일의자리수가 모두 clap에 들어있는 경우
    elif str_count[j][1:] in clap:
        str_count[j] = "-"
    elif str_count[j][:1] in clap:
        str_count[j] = "-"

print(*str_count)






















