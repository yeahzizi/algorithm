N = int(input())
step = list(str(input()))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

visited = []
r, c, dir = 0, 0, 0 #dir은 방향

Q = [[0, 0]]


for i in step:
    if i == 'F':
        r += dr[dir % 4]
        c += dc[dir % 4]
    elif i == "R":  #오른쪽 보기
        dir += 1
    elif i == "L":  #왼쪽 보기
        dir += 3







print(f'#{tc} {dfs()}')


