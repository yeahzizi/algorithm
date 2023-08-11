for _ in range(int(input())):
    num = list(map(int, input().split()))
    num.sort()
    print(num[-3])