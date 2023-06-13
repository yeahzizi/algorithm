n, m = map(int, input().split())
word = []

for i in range(n):
    word.append(input())

cnt = {}
for i in range(n):
    if len(word[i]) >= m:
        cnt[word[i]] += 1

