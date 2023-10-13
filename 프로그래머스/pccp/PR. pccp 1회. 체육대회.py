from itertools import permutations


def solution(ability):
    answer = 0
    # 종목 수
    n = len(ability[0])
    case = list(permutations(ability, n))

    for i in range(len(case)):
        cnt = 0
        for j in range(len(case[i])):
            cnt += case[i][j][j]
        answer = max(answer, cnt)
    return answer