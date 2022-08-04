T = int(input())

for test_case in range(1, T + 1):
    n = input()
    thirty_one = ("01", "03", "05", "07", "08", "10", "12")
    thirty = ("04", "06", "09", "11")

    if (n[4:6] == "02") and (1 <= int(n[6:]) <= 28):
        print ('#%d'%test_case, f'{n[:4]}/{n[4:6]}/{n[6:]}')
    elif (n[4:6] in thirty_one) and (1 <= int(n[6:]) <= 31):
        print ('#%d'%test_case, f'{n[:4]}/{n[4:6]}/{n[6:]}')
    elif (n[4:6] in thirty) and (1 <= int(n[6:]) <= 30):
        print ('#%d'%test_case, f'{n[:4]}/{n[4:6]}/{n[6:]}')
    else:
        print('#%d'%test_case, -1)
    
        

    
        


     


