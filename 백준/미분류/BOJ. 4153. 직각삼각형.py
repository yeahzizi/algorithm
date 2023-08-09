while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break

    max_num = max(num)
    min_num = min(num)
    num.remove(max_num)
    num.remove(min_num)

    if max_num ** 2 == min_num ** 2 + num[0] ** 2:
        print("right")
    else:
        print("wrong")
