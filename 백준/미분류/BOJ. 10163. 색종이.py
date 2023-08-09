#범위 안에 t를 넣어주고, t의 개수를 센다.
T = int(input())
space = [[0] * 1001 for _ in range(1001)]
#가로, 세로 1001칸으로 구성된 격자 모양을 만듦

for t in range(1, T+1):
    x, y, wid, hei = map(int, input().split())
    for i in range(x, x+wid):
        for j in range(y, y+hei):
            space[i][j] = t #범위 안에 t를 넣어준다.

for t in range(1, T+1):
    count = 0
    for j in space: #space에 t가 있는지 찾고 더한다. > 여기서 시간초과 인듯..
        count += j.count(t)
    print(count)



