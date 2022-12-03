from collections import Counter

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

counter1=Counter(arr1)

for num in arr2:
    if num in counter1:
        print(counter1[num], end=' ')
    else:
        print(0, end=' ')
