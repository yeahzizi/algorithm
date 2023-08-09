N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = []
diff = 0
min_diff = 9999999
result = 0

for i in range(N):       #순열로 5개중에 3개를 뽑아서 더해준 다음 리스트에 넣는다.
    for j in range(N):
        for k in range(N):
            if i != j and j != k and i != k:
                ans.append(cards[i]+cards[j]+cards[k])

for i in ans:
    diff = M-i   #M과 i의 차이가 작을 수록 갱신한다.
    if 0 <= diff < min_diff:
        min_diff = diff
        result = i   #M과 i의 차이가 가장 작으면 답이 된다.

print(result)




