# 쉽게쉽게 생각하기

def solution(n):
    ans = 1

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            ans += 1

    return ans