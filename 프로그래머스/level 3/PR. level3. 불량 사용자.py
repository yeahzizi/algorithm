answer = []
def dfs(banned, banned_id, idx, visited):
    if idx == len(banned_id):
        if set(visited) not in answer:
            answer.append(set(visited))
        return

    now = banned_id[idx]
    for i in range(len(banned[banned_id[idx]])):
        print(banned_id[idx])
        if banned[now][i] in visited:
            continue
        visited.append(banned[now][i])
        dfs(banned, banned_id, idx + 1, visited)
        visited.pop()


def solution(user_id, banned_id):
    banned = dict()

    for ban in banned_id:
        banned[ban] = []

    for ban in banned_id:
        for use in user_id:
            if len(ban) != len(use):
                continue
            else:
                for i in range(len(ban)):
                    if ban[i] == "*":
                        continue
                    elif ban[i] != use[i]:
                        break
                else:
                    if use not in banned[ban]:
                        banned[ban].append(use)
    dfs(banned, banned_id, 0, [])
    return len(answer)
