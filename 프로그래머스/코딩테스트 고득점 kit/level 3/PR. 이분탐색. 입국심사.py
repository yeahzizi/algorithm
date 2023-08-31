def solution(n, times):
    start = times[0]
    end = times[0] * n

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for t in times:
            cnt += mid // t

        if cnt >= n:
            answer = mid
            end = mid - 1
        elif cnt < n:
            start = mid + 1

    return answer