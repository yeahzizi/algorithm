T = int(input())

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    even = []
    odd = []

    for i in range(len(num)):
        if i % 2 == 0:
            even.append(num[i])
        else:
            odd.append(num[i])

    p = [0] * (N + 1)

    for i in range(N+1):
        make_set(i)

    cnt = 0

    for i in range(len(even)):
        if find_set(even[i]) != find_set(odd[i]):
            union(even[i], odd[i])
            cnt += 1

        if cnt == N:
            break

    answer = set()
    for i in p:
        #if p[i] not in answer:
        answer.add(find_set(i))

    print(f'#{tc} {len(answer)-1}')




