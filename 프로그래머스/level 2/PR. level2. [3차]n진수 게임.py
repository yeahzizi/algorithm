def solution(n, t, m, p):
    answer = '01'
    game = "0123456789ABCDEF"

    for i in range(2, t * m):
        result = ''
        while i > 0:
            nameji = i % n
            i = i // n
            result += game[nameji]
        answer += result[::-1]

    return answer[p - 1::m][:t]