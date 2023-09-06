N, M = map(int, input().split())
num = list(map(int, input().split())) +[1e9]
num.sort()
ans = []
used = [False] * (N+1)

def back_tracking():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(N):
        if not used[i]:
            if i > 0 and num[i] == num[i-1] and not used[i-1]:
                continue

            else:
                used[i] = True
                ans.append(num[i])
                back_tracking()
                ans.pop()
                used[i] = False


back_tracking()