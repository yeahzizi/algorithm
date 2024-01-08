def solution(lottos, win_nums):
    answer = []
    price = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    cnt = 0
    zero = 0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            zero += 1

    answer.append(price[cnt])
    answer.append(price[cnt + zero])
    answer.sort()

    return answer