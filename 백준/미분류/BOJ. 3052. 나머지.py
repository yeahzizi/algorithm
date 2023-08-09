nums = [int(input()) for i in range(10)]
remainder = []

for i in nums:
    remainder.append(i % 42)

print(len(set(remainder)))