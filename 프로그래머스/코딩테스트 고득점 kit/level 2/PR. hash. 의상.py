# 딕셔너리
def solution(clothes):
    answer = 1
    comb = dict()

    for i, j in clothes:
        comb.setdefault(j, 0)
        comb[j] = comb[j] + 1

    for key, value in comb.items():
        answer *= (value + 1)

    return answer - 1