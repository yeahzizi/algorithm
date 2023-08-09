N, M = list(map(int, input().split()))
width = [0, N] #0과 가장 큰 값인 N값을 미리 리스트에 넣는다.
height = [0, M]

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())
    if x == 1: #잘라질 번호들을 미리 세팅한 리스트에 넣는다.
        width.append(y)
    if x == 0:
        height.append(y)

width.sort() #번호가 순서대로 나열되도록 오름차순으로 정렬한다.
height.sort() #(잘라질 번호들이 나중에 들어갔으므로)

max_width = 0
max_height = 0

for i in range(len(width)-1): #번호들의 차이가 가장 큰 값이 max 값이 된다.
    if max_width < width[i+1] - width[i]:
        max_width = width[i+1] - width[i]
for j in range(len(height)-1):
    if max_height < height[j+1] - height[j]:
        max_height = height[j+1] - height[j]

print(max_width * max_height)
