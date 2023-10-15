# 투포인터
def solution(sequence, k):
    answer = []
    end = 0
    cnt = 0

    for i in range(len(sequence)):
        while end < len(sequence) and cnt < k:
            cnt += sequence[end]
            end += 1

        if cnt == k:
            if not answer:
                answer = [i, end - 1]
            else:
                if answer[1] - answer[0] <= end - 1 - i:
                    answer = answer
                else:
                    answer = [i, end - 1]
        cnt -= sequence[i]

    return answer