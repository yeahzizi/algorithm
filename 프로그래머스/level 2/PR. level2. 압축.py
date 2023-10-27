def solution(msg):
    answer = []
    num = dict()

    for i in range(26):
        num[chr(65 + i)] = i + 1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(num[msg[w:c]])
            break
        if msg[w:c + 1] not in num:
            num[msg[w:c + 1]] = len(num) + 1
            answer.append(num[msg[w:c]])
            w = c

    return answer