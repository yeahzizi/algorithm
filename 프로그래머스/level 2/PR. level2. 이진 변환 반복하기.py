def solution(s):
    answer = []
    zero = 0
    cnt = 0

    while True:
        if s == "1":
            break
        zero += s.count("0")
        s = s.replace("0", "")
        c = len(s)
        s = str(bin(c)[2:])
        cnt += 1

    answer.append(cnt)
    answer.append(zero)

    return answer