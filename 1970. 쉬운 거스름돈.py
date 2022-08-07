T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    dict_money = {"50000": 0, "10000": 0, "5000":0, "1000":0, "500":0, "100":0, "50":0, "10":0}

    for money in dict_money.keys():
       dict_money[money] = str(n // int(money))
       n %= int(money)
    
    print('#%d'%test_case)
    print(" ".join(dict_money.values()))