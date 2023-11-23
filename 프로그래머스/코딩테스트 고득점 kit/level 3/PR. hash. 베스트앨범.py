from collections import defaultdict


def solution(genres, plays):
    answer = []
    song = defaultdict(list)

    for i in range(len(genres)):
        song[genres[i]].append([plays[i], i])
    song = sorted(song.items(), key=lambda x: sum(play[0] for play in x[1]), reverse=True)

    for genres, play in song:
        play = sorted(play, key=lambda x: x[0], reverse=True)
        if len(play) == 1:
            answer.append(play[0][1])
        else:
            answer.append(play[0][1])
            answer.append(play[1][1])

    return answer