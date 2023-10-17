def solution(s):
    answer = 1

    def pali(x):
        if x == x[::-1]:
            return True
        else:
            return False

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if pali(s[i:j]):
                answer = max(answer, len(s[i:j]))

    return answer