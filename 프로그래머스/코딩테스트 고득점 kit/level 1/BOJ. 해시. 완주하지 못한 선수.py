def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(0)
    answer = ''

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer += participant[i]
            break
    return answer