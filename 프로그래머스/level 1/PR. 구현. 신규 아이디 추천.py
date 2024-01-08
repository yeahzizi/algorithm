def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    new_id = list(new_id)
    n = len(new_id)

    # 2
    for i in range(n):
        if new_id[i].isalnum() != True and new_id[i] != "-" and new_id[i] != "_" and new_id[i] != ".":
            new_id[i] = ""

    new_id = "".join(new_id)
    new_id = list(new_id)

    # 3
    for i in range(len(new_id) - 1):
        if new_id[i] == "." and new_id[i + 1] == ".":
            new_id[i] = ""
    new_id = "".join(new_id)

    # 4
    if len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    # 5
    if len(new_id) == 0:
        new_id += "a"

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # 7
    if len(new_id) < 3:
        while len(new_id) < 3:
            word = new_id[-1]
            new_id += word

    return new_id