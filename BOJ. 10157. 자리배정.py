#델타검색
#공연장을 오른쪽으로 반바퀴 돌린 상태에서 푼다.
#공연장의 크기보다 대기 순서가 크면 0이 나오도록 한다.

C, R = map(int, input().split())
K = int(input())

sit = [[0] * R for _ in range(C)]
ticket = 1
r, c = -1, 0
dir = 0

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

if K > C * R:
    print(0)

while ticket <= C * R:
    r, c = r + dr[dir], c + dc[dir]
    if 0 <= c < C and 0 <= r < R and sit[c][r] == 0:
        sit[c][r] = ticket
        ticket += 1
    else:
        r, c = r - dr[dir], c - dc[dir]
        dir = (dir + 1) % 4

for x in range(C):
    for y in range(R):
        if sit[x][y] == K:
            print(x+1, y+1)
            break

