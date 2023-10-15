def solution(s):
    answer = ''
    arr = s.split(" ")
    max_num = -987654321
    min_num = 987654321

    for i in arr:
        max_num = max(max_num, int(i))
        min_num = min(min_num, int(i))
    answer = str(min_num) + " " + str(max_num)

    return answer