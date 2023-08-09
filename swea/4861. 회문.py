T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    p_matrix = [input() for _ in range(N)]
    p_zip = list(map(list, zip(*p_matrix))) #에스터리스크를 넣으면 매트릭스 전체가 비교된다.(세로도 비교해야 하니 zip 사용)
    palindrome = ""

    for i in range(N):
        for j in range(N-M+1):
            if p_matrix[i][j:j+M] == p_matrix[i][j:j+M][::-1]: #앞에서 시작할 때와 뒤에서 시작할 때가 같으면,
                palindrome = p_matrix[i][j:j+M] #palindrome에 넣는다.
                break
            if p_zip[i][j:j+M] == p_zip[i][j:j+M][::-1]: #세로 묶음에도 회문이 있는지 찾기
                palindrome = "".join(p_zip[i][j:j+M]) #문자열을 합쳐서 반환
                break

    print(f'#{test_case} {palindrome}')






