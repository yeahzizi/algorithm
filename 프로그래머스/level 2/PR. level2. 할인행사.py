def solution(want, number, discount):
    answer = 0
    deserve = 10
    check = dict()

    for w in range(len(want)):
        check.setdefault(want[w], number[w])

    for i in range(len(discount) - deserve + 1):
        cnt = {}
        for j in range(i, deserve + i):
            cnt.setdefault(discount[j], 0)
            cnt[discount[j]] += 1
        if cnt == check:
            answer += 1

    return answer