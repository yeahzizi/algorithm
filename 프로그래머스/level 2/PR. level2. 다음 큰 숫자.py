def solution(n):
    answer = 0
    one = str(bin(n)[2:])
    one = one.count("1")

    while True:
        n += 1
        check = str(bin(n)[2:])
        check = check.count("1")
        if check == one:
            answer += n
            break

    return answer