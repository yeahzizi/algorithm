def solution(answers):
    one = [1, 2, 3, 4, 5]  # 1번 수포자 패턴
    two = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번 수포자 패턴
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자 패턴

    # 수포자 정답 체크
    ans = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            ans[0] += 1
        if answers[i] == two[i % len(two)]:
            ans[1] += 1
        if answers[i] == three[i % len(three)]:
            ans[2] += 1

    # 체크한 정답 수가 가장 많이 맞춘 정답 수와 같다면 answer에 인덱스+1(수포자 번호) 추가
    answer = []
    for i in range(len(ans)):
        if ans[i] == max(ans):
            answer.append(i + 1)

    return answer