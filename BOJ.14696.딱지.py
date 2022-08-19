T = int(input())
N = [list(map(int, input().split())) for _ in range(2*T)]
A = []
B = []

for i in range(2 * T): #A와 B를 각각 다른 리스트에 넣어준다.
    if i % 2:
        B.append(N[i])
    else:
        A.append(N[i])

for j in range(T): #[1:]을 이용해서 앞에 a,b는 제외하고 카운트해서 비교
    if (4 in A[j][1:] or 4 in B[j][1:]) and (A[j][1:].count(4) > B[j][1:].count(4)):
        print("A")
        continue #조건에 맞으면 continue 해서 다시 반복하기
    elif (4 in A[j][1:] or 4 in B[j][1:]) and (A[j][1:].count(4) < B[j][1:].count(4)):
        print("B")
        continue
    elif (4 in A[j][1:] or 4 in B[j][1:]) and (A[j][1:].count(4) == B[j][1:].count(4)):
        if A[j][1:].count(3) > B[j][1:].count(3):
            print("A")
            continue
        elif A[j][1:].count(3) < B[j][1:].count(3):
            print("B")
            continue
        elif A[j][1:].count(3) == B[j][1:].count(3):
            if A[j][1:].count(2) > B[j][1:].count(2):
                print("A")
                continue
            elif A[j][1:].count(2) < B[j][1:].count(2):
                print("B")
                continue
            elif A[j][1:].count(2) == B[j][1:].count(2):
                if A[j][1:].count(1) > B[j][1:].count(1):
                    print("A")
                    continue
                elif A[j][1:].count(1) < B[j][1:].count(1):
                    print("B")
                    continue
                elif A[j][1:].count(1) == B[j][1:].count(1):
                    print("D")
                    continue
    if (3 in A[j][1:] or 3 in B[j][1:]) and (A[j][1:].count(3) > B[j][1:].count(3)):
        print("A")
        continue
    if (3 in A[j][1:] or 3 in B[j][1:]) and (A[j][1:].count(3) < B[j][1:].count(3)):
        print("B")
        continue
    if (3 in A[j][1:] or 3 in B[j][1:]) and (A[j][1:].count(3) == B[j][1:].count(3)):
        if A[j][1:].count(2) > B[j][1:].count(2):
            print("A")
            continue
        if A[j][1:].count(2) < B[j][1:].count(2):
            print("B")
            continue
        if A[j][1:].count(2) == B[j][1:].count(2):
            if A[j][1:].count(1) > B[j][1:].count(1):
                print("A")
                continue
            if A[j][1:].count(1) < B[j][1:].count(1):
                print("B")
                continue
            if A[j][1:].count(1) == B[j][1:].count(1):
                print("D")
                continue
    if (2 in A[j][1:] or 2 in B[j][1:]) and (A[j][1:].count(2) > B[j][1:].count(2)):
        print("A")
        continue
    if (2 in A[j][1:] or 2 in B[j][1:]) and (A[j][1:].count(2) < B[j][1:].count(2)):
        print("B")
        continue
    if (2 in A[j][1:] or 2 in B[j][1:]) and (A[j][1:].count(2) == B[j][1:].count(2)):
        if A[j][1:].count(1) > B[j][1:].count(1):
            print("A")
            continue
        if A[j][1:].count(1) < B[j][1:].count(1):
            print("B")
            continue
        if A[j][1:].count(1) == B[j][1:].count(1):
            print("D")
            continue
    if (1 in A[j][1:] or 1 in B[j][1:]) and (A[j][1:].count(1) > B[j][1:].count(1)):
        print("A")
        continue
    if (1 in A[j][1:] or 1 in B[j][1:]) and (A[j][1:].count(1) < B[j][1:].count(1)):
        print("B")
        continue
    if (1 in A[j][1:] or 1 in B[j][1:]) and (A[j][1:].count(1) == B[j][1:].count(1)):
        print("D")
        continue

'''
        for s in range(4):
            if ttakji_A[s] > ttakji_B[s]:
                print("A")
            elif ttakji_A[s] < ttakji_B[s]:
                print("B")
        else:
            print("D")
'''



'''
    for i in range(2*T):
        if i % 2:
            B.append(N[i])
        else:
            A.append(N[i])

    for j in range(T):
        for s in range(1, T):
            print(A)
            if A[j][s] == 4:
                ttakji_dict_A[4] += 1
            if A[j][s] == 3:
                ttakji_dict_A[3] += 1
            if A[j][s] == 2:
                ttakji_dict_A[2] += 1
            if A[j][s] == 1:
                ttakji_dict_A[1] += 1

    print(ttakji_dict_A)


        if 4 in B[j][1:]:
            ttakji_dict_B[4] += B[j].count(4)
        if 3 in B[j][1:]:
            ttakji_dict_B[3] += B[j].count(3)
        if 2 in B[j][1:]:
            ttakji_dict_B[2] += B[j].count(2)
        if 1 in B[j][1:]:
            ttakji_dict_B[1] += B[j].count(1)
            
                        if ttakji_dict_A[4] > ttakji_dict_B[4]:
                print(A)
            if ttakji_dict_A[4] < ttakji_dict_B[4]:
                print(B)
            if ttakji_dict_A[4] == ttakji_dict_B[4]:
                if ttakji_dict_A[3] > ttakji_dict_B[3]:
                    print(A)
                if ttakji_dict_A[3] < ttakji_dict_B[3]:
                    print(B)
                if ttakji_dict_A[3] == ttakji_dict_B[3]:
                    if ttakji_dict_A[2] > ttakji_dict_B[2]:
                        print(A)
                    if ttakji_dict_A[2] < ttakji_dict_B[2]:
                        print(B)
                    if ttakji_dict_A[2] == ttakji_dict_B[2]:
                        if ttakji_dict_A[1] > ttakji_dict_B[1]:
                            print(A)
                        if ttakji_dict_A[1] < ttakji_dict_B[1]:
                            print(B)
                        if ttakji_dict_A[1] < ttakji_dict_B[1]:
                            print(B)
                        if ttakji_dict_A[1] == ttakji_dict_B[1]:
                            print(D)

    for j in range(T):
        if 4 in A[j][1:] or 4 in B[j][1:]:
            ttakji_A[0] += A[j].count(4)
            ttakji_B[0] += B[j].count(4)
        if 3 in A[j][1:] or 3 in B[j][1:]:
            ttakji_A[1] += A[j].count(3)
            ttakji_B[1] += B[j].count(3)
        if 2 in A[j][1:] or 2 in B[j][1:]:
            ttakji_A[2] += A[j].count(2)
            ttakji_B[2] += B[j].count(2)
        if 1 in A[j][1:] or 1 in B[j][1:]:
            ttakji_A[3] += A[j].count(1)
            ttakji_B[3] += B[j].count(1)
'''






