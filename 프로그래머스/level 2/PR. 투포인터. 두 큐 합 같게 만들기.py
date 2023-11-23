# 먼말인지 모르겠음..
def solution(queue1, queue2):
    n = len(queue1)
    q = queue1 + queue2
    target = sum(q)
    if target % 2 != 0:
        return -1
    target //= 2

    ans = 987654321
    en = 0
    tot = q[0]

    for st in range(2 * n):
        while tot < target:
            en = (en + 1) % (2 * n)
            tot += q[en]

        if tot == target:
            moves = 0
            if en < n - 1:
                moves = 3 * n + 1 + st + en
            else:
                moves = st + (en - n + 1)
            ans = min(ans, moves)

        tot -= q[st]

    if ans == 987654321:
        ans = -1
    return ans