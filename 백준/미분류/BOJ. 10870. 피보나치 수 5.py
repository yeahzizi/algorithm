def a(n):
    if n <= 1:
        return n
    return a(n-1) + a(n-2)

n = int(input())
print(a(n))