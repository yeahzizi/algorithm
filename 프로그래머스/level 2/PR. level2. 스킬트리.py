def check(word, skill):
    now, idx = skill[0], 0
    for i in word:
        if i in skill and now != i:
            return 0
        elif i == now:
            if idx + 1 == len(skill):
                return 1
            now, idx = skill[idx + 1], idx + 1
    return 1


def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)

    for s in skill_trees:
        answer += check(s, skill)

    return answer