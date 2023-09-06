N, M = map(int, input().split())
ans = []

def back_tracking():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1):
        ans.append(i)
        back_tracking()
        ans.pop()

back_tracking()
