def solution(A, B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort()

    i, j = 0, 0
    while True:
        if j == n:
            break
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1

    return answer