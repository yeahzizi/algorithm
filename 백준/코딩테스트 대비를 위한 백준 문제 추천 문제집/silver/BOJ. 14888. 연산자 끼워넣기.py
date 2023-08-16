#백트래킹
#재귀호출이 스택에 쌓이면 => 이걸 하나씩 꺼낸다? 이런 개념??
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split())) #+, -, *, %

maximum = -1999999999
minimum = 1999999999

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    #종료조건
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], cal[0], cal[1], cal[2], cal[3])
print(maximum)
print(minimum)