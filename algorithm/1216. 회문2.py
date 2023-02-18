for test_case in range(10):
    T = int(input())
    p_matrix = [input() for _ in range(100)]
    p_zip = list(map(list, zip(*p_matrix)))
    max_palindrome = 0

    for M in range(100, -1, -1):
        for i in range(100):
            for j in range(100-M+1):
                if p_matrix[i][j:M+j] == p_matrix[i][j:j+M][::-1]: #앞에서 시작할 때와 뒤에서 시작할 때가 같으면,
                    max_palindrome = max(max_palindrome, M) #palindrome에 넣는다.
                if p_zip[i][j:j+M] == p_zip[i][j:j+M][::-1]: #세로 묶음에도 회문이 있는지 찾기
                    max_palindrome = max(max_palindrome, M)#문자열을 합쳐서 반환
                    break

    print(f'#{test_case+1} {max_palindrome}')