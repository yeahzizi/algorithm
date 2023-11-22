# 테스트 1 〉	통과 (45.37ms, 23MB)
# 테스트 2 〉	통과 (23.47ms, 17MB)
# 테스트 3 〉	통과 (64.92ms, 27MB)
# 테스트 4 〉	통과 (1.13ms, 10.4MB)
# 테스트 5 〉	통과 (41.47ms, 21.7MB)
# 테스트 6 〉	통과 (35.39ms, 20.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.02ms, 9.94MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)

def solution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = "".join(numbers)

    if answer[0] == "0":
        return "0"
    else:
        return answer

# version 2
# 완전히 이해함함
defsolution(numbers):
    answer = ''

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'
    return answer