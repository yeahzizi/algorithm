def solution(sizes):
    switch = 0
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            switch = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = switch

    max_hight = 0
    max_width = 0
    for i in range(len(sizes)):
        if sizes[i][0] > max_width:
            max_width = sizes[i][0]
        if sizes[i][1] > max_hight:
            max_hight = sizes[i][1]

    answer = 0
    answer = max_hight * max_width

    return answer