base = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
    'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32,
    'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40,
    'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48,
    'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56,
    '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63
}

T = int(input())
for tc in range(1, T+1):
    S = input()
    decode = ''
    binary = 0
    result = ''

    for c in S:
        binary = bin(base[c])   #bin을 사용해서 2진수로 바꿔준다.
        decode = str(binary[2:])  #bin을 사용하면 앞에 0b가 붙으니 그 다음부터 append

        while len(decode) < 6:  #6진수로 만들기 위해 길이가 6이 아니면 계속 0을 붙여준다.
            decode = '0' + decode
        result += decode

    ans = ''
    for i in range(0, len(result), 8):
        ans += chr(int(result[i:i+8], base = 2))
    print(f'#{tc} {ans}')




