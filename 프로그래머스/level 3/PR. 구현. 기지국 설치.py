def solution(n, stations, w):
    answer = 0

    left = 1
    for i in stations:
        r1 = i - w
        r2 = i + w
        if r1 > left:
            answer += (r1 - left) // (2 * w + 1)
            if (r1 - left) % (2 * w + 1) != 0:
                answer += 1
        if stations[-1] == i:
            if n > r2:
                answer += (n - r2) // (2 * w + 1)
                if (n - r2) % (2 * w + 1) != 0:
                    answer += 1
        else:
            left = r2 + 1

    return answer
