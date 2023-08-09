place = input()
row = int(place[1]) #행
# ord()을 이용해 문자를 유니코드 값으로 변환
# a1이라는 좌표를 쉽게 나타내기 위해 => a는 1, b는 2... 가 되도록 변환
column = int(ord(place[0])) - int(ord('a')) + 1 #열
steps = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row <= 8 and 1<= next_row and next_column <= 8 and 1 <= next_column:
        result += 1

print(result)