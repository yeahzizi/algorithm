import sys

n, k = map(int, input().split())
rate = list(map(int, input().split()))
arr = []

for _ in range(k):
    a, b = map(int, input().split())
    arr.append([a-1, b-1])

for i, j in arr:
    if i <= j:
        hap = sum(rate[i:j+1])
        print("{:.2f}".format(round(hap / (j-i+1), 3)))
    else:
        hap = sum(rate[j:i+1])
        print("{:.2f}".format(round(hap / (i-j+1), 3)))