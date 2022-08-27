score_sum = 0
for t in range(5):
    score = int(input())

    if score < 40:
        score_sum += 40
    else:
        score_sum += score
print(score_sum // 5)

