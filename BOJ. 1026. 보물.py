#A의 가장 작은 수와 B의 가장 큰 수를 곱하는 방식
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()             #A는 오름차순 정렬
B.sort(reverse=True) #B는 내림차순 정렬

sum = 0
for i in range(N):
    sum += A[i] * B[i]   #정렬 후 곱해서 더하면 최소값이 된다.
    continue

print(sum)
