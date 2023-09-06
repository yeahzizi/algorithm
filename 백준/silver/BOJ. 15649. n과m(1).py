# 백트래킹
N, M = map(int, input().split())
ans = []

def back_tracking():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back_tracking() #재귀
            ans.pop() #return 후에 실행
            # 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것

back_tracking()