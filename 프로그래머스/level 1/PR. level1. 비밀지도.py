def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        new = ""
        s1 = bin(arr1[i])[2:].zfill(n)
        s2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if s1[j] == "1" or s2[j] == "1":
                new += "#"
            else:
                new += " "
        answer.append(new)

    return answer