import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))

    for i in range(N-1, -1, -1):
        end = num[N-1] #마지막 값을 갱신하기
        if





