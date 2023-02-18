T = int(input())
for i in range(1, T + 1):
    number_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    TC = list(input().split())
    number = list(input().split())
    number_integer = []
    number_list = []

    for key, value in number_dict.items(): #.items를 이용해 key와 value 값을 불러낸다.
        for k in range(len(number)):
            if key == number[k]: #key 값과 number의 값이 같으면 빈 리스트에 vlaue 값을 넣어준다.
                number_integer.append(value) #오름차순 정렬 완료

    for key, value in number_dict.items(): #number_integer 에는 정수만 담겨 있으므로 다시 문자인 key 값으로 바꿔준다.
        for j in range(len(number_integer)):
            if value == number_integer[j]:
                number_list.append(key)

    print(TC[0])
    print(*number_list)





