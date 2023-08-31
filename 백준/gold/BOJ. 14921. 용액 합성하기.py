N = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1

ans = 1000000001
cnt = 0
while start < end:
    mid = array[start]+array[end]
    zero = 0

    if mid >= zero:
        end -= 1
        if abs(ans) > abs(mid-zero):
            ans = mid-zero
        else:
            ans = ans

    else:
        start += 1
        if abs(ans) > abs(mid - zero):
            ans = mid - zero
        else:
            ans = ans

print(ans)