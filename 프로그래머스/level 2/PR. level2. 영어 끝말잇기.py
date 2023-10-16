def solution(n, words):
    answer = []
    cnt = [0] * len(words)

    a, b = 0, 0
    for i in range(len(words)):
        if words[i] in words[:i]:
            a = (i) // n + 1
            b = (i + 1) % n
            break
        if i > 0 and words[i - 1][-1] != words[i][0]:
            a = (i) // n + 1
            b = (i + 1) % n
            break

    if a != 0 and b == 0:
        b += n
    answer.append(b)
    answer.append(a)
    return answer