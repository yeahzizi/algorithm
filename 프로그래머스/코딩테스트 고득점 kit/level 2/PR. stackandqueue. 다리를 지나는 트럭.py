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


