def factorial(depth):
    result = 1
    if depth > 0:
        result = depth * factorial(depth-1)
    return result

depth = int(input())
print(factorial(depth))
