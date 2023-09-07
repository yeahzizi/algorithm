# 숫자 카운트 문제
# 0~9 이런식으로 나오면 카운트 해서 푸는 방법 떠올리기
N = int(input())
card = [0] * 10

for i in str(N):
    if i == "6" or i == "9":
        if card[6] >= card[9]:
            card[9] += 1
        else:
            card[6] += 1
    else:
        card[int(i)] += 1

print(max(card))