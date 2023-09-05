N, K = map(int, input().split())
word = []
for _ in range(N):
    w = input().replace("anta", "").replace("tica", "")
    word.append(w)

cnt = {"b": 0, "d":0, "e":0, "f":0, "g":0, "h":0, "o": 0,
"j":0, "k":0, "l":0, "m":0, "p":0, "q":0, "r":0, "s":0,
"u":0, "v":0, "w":0, "x":0, "y":0, "z":0}

for i in word:
    for j in set(i):
        if j == "a" or j == "n" or j == "c" or j == "t" or j == "i":
            continue
        else:
            cnt[j] += 1

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

default = ["a", "n", "t", "i", "c"]

for i in range(K-5):
    default.append(cnt[i][0])

ans = 0

def count_readable(word, default):
    result = 0
    for j in range(len(word)):
        if word[j] in default:
            result += 1
    return result

if K >= 5:
    for w in word:
        if count_readable(w, default) == len(w):
            ans += 1
else:
    ans = 0

print(ans)