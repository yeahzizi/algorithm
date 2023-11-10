def solution(record):
    answer = []
    id = dict()
    for re in record:
        parts = re.split(" ")
        if parts[0] == "Enter":
            id.setdefault(parts[1], [])
            id[parts[1]].append(parts[2])
            answer.append(f"{parts[1]}님이 들어왔습니다.")
        elif parts[0] == "Leave":
            answer.append(f"{parts[1]}님이 나갔습니다.")
        elif parts[0] == "Change":
            id[parts[1]].append(parts[2])

    for i in range(len(answer)):
        idx = answer[i].find("님")
        user = answer[i][:idx]
        answer[i] = answer[i].replace(user, id[user][-1])

    return answer