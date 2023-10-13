def solution(input_string):
    answer = []

    check = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
             'l': 0, 'm': 0, 'n': 0, 'p': 0, 'o': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for i in range(len(input_string)):
        now = input_string[i]
        if check[now] == 0:
            check[now] = 1
        elif check[now] == 1:
            if now == input_string[i - 1]:
                continue
            else:
                if now not in answer:
                    answer.append(now)

    answer.sort()
    if not answer:
        return "N"

    return "".join(map(str, answer))