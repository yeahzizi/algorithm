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
