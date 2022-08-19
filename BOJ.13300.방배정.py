import math
N, K = map(int, input().split())
personal = [input() for _ in range(N)]
room_dict = {"1 1":0, "1 2":0, "1 3":0, "1 4":0, "1 5":0, "1 6":0,
            "0 1":0, "0 2":0, "0 3":0, "0 4":0, "0 5":0, "0 6":0}


for i in range(N):
    for key in room_dict.keys():
        if key == personal[i]:
            room_dict[key] += 1
room = 0
for val in room_dict.values():
    if val >= K:
        val = math.ceil(val / K)
        room += val
    else:
        room += val


print(room)








