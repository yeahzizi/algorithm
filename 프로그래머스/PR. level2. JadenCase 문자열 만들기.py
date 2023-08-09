def solution(s):
    s = s.lower()
    answer = ''
    for i in range(len(s)):
        if s[i-1] == " " or i == 0:
            answer += ""
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer