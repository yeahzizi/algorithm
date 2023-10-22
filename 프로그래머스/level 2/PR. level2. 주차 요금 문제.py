def solution(fees, records):
    answer = []
    new = []
    for i in records:
        new.append(i.split(" "))
    record = dict()
    for n in new:
        record.setdefault(n[1], [])
        record[n[1]] += [n[0]]

    for key, value in record.items():
        fee = 0
        time = 0
        while value:
            if len(value) == 1:
                value.append("23:59")
            IN = value.pop(0)
            OUT = value.pop(0)
            hour = int(OUT[:2]) - int(IN[:2])
            mini = int(OUT[3:]) - int(IN[3:])
            if mini < 0:
                hour -= 1
                mini = (60 - int(IN[3:])) + int(OUT[3:])
            time += mini + (hour * 60)
        if time <= fees[0]:
            fee += fees[1]
        else:
            fee += fees[1]
            time -= fees[0]
            plus = time // fees[2]
            if time % fees[2] == 0:
                fee += (plus * fees[3])
            else:
                plus += 1
                fee += (plus * fees[3])
        answer.append([int(key), fee])
        answer.sort()

    return [answer[i][1] for i in range(len(answer))]