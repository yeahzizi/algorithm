#import 아니면 해결을 못하나 어이가 없다..
#최소공배수는 lcm??
#근데 for문 안의 식 자체가 최소공배수를 구하는거임
import math

def solution(arr):
    answer = 1
    for i in arr:
        answer = answer * i // math.gcd(answer, i)

    return answer