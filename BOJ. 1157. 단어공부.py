word = input()
word = word.upper()
word_dict = {letter : 0 for i, letter in enumerate(word)}
num = -900701247820

for i in word:
    word_dict[i] += 1

for i, j in word_dict.items():
    if j > num:
        num = j
        ans = i
    elif j == num:
        ans = "?"

print(ans)


