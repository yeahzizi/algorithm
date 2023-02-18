for test_case in range(10):
    idx = int(input())
    N = input()
    M = input()
    count = []

    count = M.split(N) #split 함수를 이용하여 M 안에 N이 있으면 N을 기준으로 나눠서 리스트에 저장

    print('#%d %d'%(idx, len(count)-1))

print(number_integer)

    for i in range(len(number)-1, 0, -1):
        for j in range(0, i):
            if number[j] < number[j+1]:
                number[j], number[j + 1] = number[j + 1], number[j]