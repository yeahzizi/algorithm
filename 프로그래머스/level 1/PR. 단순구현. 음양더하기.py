def solution(absolutes, signs):
    answer = 0
    n = len(absolutes)

    for i in range(n):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += (-1 * absolutes[i])

    return answer