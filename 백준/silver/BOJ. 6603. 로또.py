def back_tracking():
    if len(ans) == 6:
        print(" ".join(map(str, ans)))
        return
    for i in range(len(num)):
        if num[i] not in ans:
            if len(ans) > 0:
                if num[i] > ans[-1]:
                    ans.append(num[i])
                    back_tracking()
                    ans.pop()
            else:
                ans.append(num[i])
                back_tracking()
                ans.pop()


while True:
    num = list(map(int, input().split()))
    N = num[0]
    if len(num) == 1 and N == 0:
        break
    num = num[1:]
    ans = []
    back_tracking()
    print()