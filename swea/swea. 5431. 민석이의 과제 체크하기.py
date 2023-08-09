for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    student = [i for i in range(1, N+1)] #전체 수강생 번호 리스트를 만든다.
    ans = []

    for i in student:
        if i not in submit: #제출한 목록에 없으면 ans 리스트에 append
            ans.append(i)

    print(f'#{tc}', *ans)

