T = int(input())
for test_case in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))
    str1 = list(set(str1)) #비교하기 쉽도록 str1에 중복 값을 제외하고 리스트로 만든다.
    str_dict = {}

    for i in range(len(str1)):
        if str1[i] in str2:
            str_dict[str1[i]] = str2.count(str1[i]) #str1[i]에 해당하는 str2 값의 개수를 세서 value 값으로 준다.

    print("#%d %d"%(test_case, max(str_dict.values()))) #value 값 중 가장 큰 값을 출력한다.






