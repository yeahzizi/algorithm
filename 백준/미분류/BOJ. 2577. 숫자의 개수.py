num = []
for _ in range(3):
    num.append(int(input())) #세 개의 자연수를 리스트로 입력 받는다.
result = str(num[0] * num[1] * num[2]) #입력 받은 숫자들을 곱한 후 문자로 치환

cnt = [0] * 10 #0부터 9까지 개수를 센다.
for i in result:
    cnt[int(i)] += 1 #치환된 문자를 숫자로 변환해서 카운트한다.

for i in cnt:
    print(i)