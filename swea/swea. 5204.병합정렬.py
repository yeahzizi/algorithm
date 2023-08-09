def merge_sort(input_list):  #쪼개기
    if len(input_list) == 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)  #여기까지 쪼개기

    return merge(left, right)

def merge(left, right):  #붙이기(정렬할거임)
    result = [0] * (len(left)+len(right))
    l = r = idx = 0  #앞쪽에 붙어 있어야 하니 0으로 초기화


    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1

    if left[-1] > right[-1]: #마지막 값 비교해서 크면 + 1 꼭 합칠 때 비교
        global cnt
        cnt += 1

    while l < len(left):
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        result[idx] = right[r]
        r += 1
        idx += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(A)

    print(f'#{tc}', ans[N//2], cnt)