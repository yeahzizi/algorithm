from itertools import product

def solution(word):
    answer = 0
    alp = ["A", "E", "I", "O", "U"]

    dict = []
    for i in range(1, 6):
        for j in product(alp, repeat=i):
            dict.append("".join(j))

    dict.sort()

    for i in range(len(dict)):
        if dict[i] == word:
            return i + 1