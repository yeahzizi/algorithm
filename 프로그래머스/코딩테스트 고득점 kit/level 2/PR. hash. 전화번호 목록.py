# 효율성 3&4번 시간 초과
def solution(phone_book):
    idx = 0
    while True:
        if idx == len(phone_book):
            return True
            break
        now = phone_book[idx]
        for i in range(len(phone_book)):
            if i != idx and len(now) <= len(phone_book[i]):
                if now == phone_book[i][:len(now)]:
                    return False
                    break
        else:
            idx += 1



# 전부 통과한 코드
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.00ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.00ms, 10.1MB)
# 테스트 14 〉	통과 (0.45ms, 10.2MB)
# 테스트 15 〉	통과 (0.93ms, 10.4MB)
# 테스트 16 〉	통과 (0.82ms, 10.3MB)
# 테스트 17 〉	통과 (1.11ms, 10.5MB)
# 테스트 18 〉	통과 (1.12ms, 10.3MB)
# 테스트 19 〉	통과 (0.69ms, 10.3MB)
# 테스트 20 〉	통과 (1.52ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (2.90ms, 10.9MB)
# 테스트 2 〉	통과 (2.91ms, 10.9MB)
# 테스트 3 〉	통과 (125.83ms, 30.6MB)
# 테스트 4 〉	통과 (97.38ms, 28MB)

def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        now = phone_book[i]
        if len(now) <= len(phone_book[i + 1]):
            if now == phone_book[i + 1][:len(now)]:
                answer = False
                break

    return answer

# 똑같은데 미세하게 빠름..그냥 서버 차이 인걸로
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        now = phone_book[i]
        if len(now) <= len(phone_book[i + 1]):
            if now == phone_book[i + 1][:len(now)]:
                answer = False
                break

    return answer