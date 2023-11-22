# 테스트 1 〉	통과 (0.64ms, 10.1MB)
# 테스트 2 〉	통과 (45.78ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (9.27ms, 9.93MB)
# 테스트 5 〉	통과 (288.84ms, 10.1MB)
# 테스트 6 〉	통과 (42.59ms, 10.1MB)
# 테스트 7 〉	통과 (0.49ms, 10.2MB)
# 테스트 8 〉	통과 (0.16ms, 10.1MB)
# 테스트 9 〉	통과 (2.40ms, 10.1MB)
# 테스트 10 〉	통과 (0.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.40ms, 10.2MB)
# 테스트 13 〉	통과 (0.69ms, 10.2MB)
# 테스트 14 〉	통과 (0.03ms, 10.1MB)

def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0] * bridge_length
    sum_stack = 0

    while stack:
        answer += 1
        s = stack.pop(0)
        if s > 0:
            sum_stack -= s

        if truck_weights:
            if sum_stack + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                sum_stack += truck
                stack.append(truck)
            else:
                stack.append(0)  # 다리의 길이를 유지

    return answer


#version2
def solution(bridge_length, weight, truck_weights):
    answer = 0  # 시간
    stack = [0] * bridge_length
    sum_stack = 0

    while stack:
        answer += 1
        s = stack.pop(0)
        if s > 0:
            sum_stack -= s

        if truck_weights:
            if sum_stack + truck_weights[0] <= weight:
                now = truck_weights.pop(0)
                sum_stack += now
                stack.append(now)
            else:
                stack.append(0)

    return answer