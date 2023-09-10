# bin() => 상당히 유용하다 10진수를 2진수로 바꿀 수 있음
# zfill() 도 유용하다!! 단 이때는 [2:]가 밖으로 나가니 유의할 것!

N = int(input())
code = []
opcode = {"ADD": "00000", "ADDC": "00001", "SUB": "00010",
          "SUBC": "00011", "MOV": "00100", "MOVC": "00101",
          "AND": "00110", "ANDC": "00111", "OR": "01000",
          "ORC": "01001", "NOT": "01010", "MULT": "01100",
          "MULTC": "01101", "LSFTL": "01110", "LSFTLC": "01111",
          "LSFTR": "10000", "LSFTRC": "10001", "ASFTR": "10010",
          "ASFTRC": "10011", "RL": "10100", "RLC": "10101",
          "RR": "10110", "RRC": "10111"}
for _ in range(N):
    o, d, a, b = input().split()
    code.append([o, int(d), int(a), int(b)])


for o, d, a, b in code:
    ans = ""
    ans += opcode[o]
    ans += "0"
    ans += str(bin(d))[2:].zfill(3)
    ans += str(bin(a))[2:].zfill(3)

    if ans[4] == "0":
        ans += str(bin(b))[2:].zfill(3)
        ans += "0"
    else:
        ans += str(bin(b))[2:].zfill(4)

    print(ans)


# 또 다른 코드 (심지어 이게 더 빠르고 메모리도 덜 잡아먹음)
N = int(input())
code = []
opcode = {"ADD": "00000", "ADDC": "00001", "SUB": "00010",
          "SUBC": "00011", "MOV": "00100", "MOVC": "00101",
          "AND": "00110", "ANDC": "00111", "OR": "01000",
          "ORC": "01001", "NOT": "01010", "MULT": "01100",
          "MULTC": "01101", "LSFTL": "01110", "LSFTLC": "01111",
          "LSFTR": "10000", "LSFTRC": "10001", "ASFTR": "10010",
          "ASFTRC": "10011", "RL": "10100", "RLC": "10101",
          "RR": "10110", "RRC": "10111"}
for _ in range(N):
    o, d, a, b = input().split()
    code.append([o, int(d), int(a), int(b)])


for o, d, a, b in code:
    ans = ""
    ans += opcode[o]
    ans += "0"
    rD = str(bin(d)[2:])
    if len(rD) == 1:
        ans = ans + "00" + rD
    if len(rD) == 2:
        ans = ans + "0" + rD
    if len(rD) == 3:
        ans += rD
    rA = str(bin(a)[2:])
    if len(rA) == 1:
        ans = ans + "00" + rA
    if len(rA) == 2:
        ans = ans + "0" + rA
    if len(rA) == 3:
        ans += rA
    if ans[4] == "0":
        rB = str(bin(b)[2:])
        if len(rB) == 1:
            ans = ans + "00" + rB + "0"
        if len(rB) == 2:
            ans = ans + "0" + rB + "0"
        if len(rB) == 3:
            ans += rB + "0"
    if ans[4] == "1":
        C = str(bin(b)[2:])
        if len(C) == 1:
            ans = ans + "000" + C
        if len(C) == 2:
            ans = ans + "00" + C
        if len(C) == 3:
            ans = ans + "0" + C
        if len(C) == 4:
            ans += C

    print(ans)