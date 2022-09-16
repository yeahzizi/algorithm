T = int(input())
for tc in range(1, T+1):
    mirror = {"b":"d", "d":"b", "p":"q", "q":"p"}   #거울에 비칠 문자열들을 딕셔너리로 저장
    answer = []

    for i in input():
        for key, value in mirror.items(): #딕녀서리에서 key와 value 값을 꺼내옴
            if i == key:  # input값과 key값이 같으면,
                answer.append(value)  #value를 answer 리스트에 할당

    answer = "".join(answer[::-1])  #거울에 비추면 맨 뒷 값이 처음 값이 되므로, answer 값을 뒤집음

    print(f'#{tc} {answer}')

