T = int(input())
for test_case in range(1, T + 1):
    N, M = list(input().split())
    count = []

    count = N.replace(M, "*") #replace 함수를 이용해서 N 문자열 통채로 * 로 바꾼다.
    print('#%d %d'%(test_case, len(count))) #N이 문자열 1개로 바뀌므로, len함수를 이용해 개수를 센다.
