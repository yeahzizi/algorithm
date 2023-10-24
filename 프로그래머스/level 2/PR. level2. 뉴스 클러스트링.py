# 빡구현
import math

def solution(str1, str2):
    answer = 0

    arr1 = []
    arr2 = []
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1) - 1):
        new = str1[i] + str1[i + 1]
        if new.isalpha():
            arr1.append(new)

    for i in range(len(str2) - 1):
        new = str2[i] + str2[i + 1]
        if new.isalpha():
            arr2.append(new)

    arr1.sort()
    arr2.sort()
    kyo = []
    hap = arr2.copy()
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            kyo.append(arr1[i])
            arr2.remove(arr1[i])
        else:
            hap.append(arr1[i])

    if not kyo and not hap:
        return 1 * 65536
    elif not kyo and hap:
        return 0

    return math.floor((len(kyo) / len(hap)) * 65536)