# 개오래걸림..
def solution(elements):
    n = len(elements)
    elements = elements + elements
    arr = []
    for i in range(n + 1):
        for j in range(i + 1, i + 1 + n):
            arr.append(sum(elements[i:j]))

    return len(set(arr))