def solution(array, commands):
    answer = []
    slice = []

    for i in commands:
        slice = array[i[0] - 1:i[1]]
        slice.sort()
        answer.append(slice[i[2] - 1])

    return answer