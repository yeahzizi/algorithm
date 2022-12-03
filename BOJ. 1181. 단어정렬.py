N = int(input())
words = {}

for _ in range(N):
    word = input()
    words[word] = len(word)

words = sorted(words.items(), key=lambda x:x[0])

words.sort(key=lambda x:x[1])

for i, j in words:
    print(i)
