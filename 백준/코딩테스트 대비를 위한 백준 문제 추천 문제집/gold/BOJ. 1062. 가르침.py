#시뮬레이션
#개 엉망 코드..다시풀기
N, K = map(int, input().split())
word = []
dict_word = {}
default = ['a', 'n', 't', 'i', 'c']

for i in range(N):
    all_word = input()
    word.append(all_word[4: -4])

# 중복을 제거하고 문자별 등장 횟수를 세는 과정
for w in word:
    unique_chars = set(w)
    for char in unique_chars:
        if char not in dict_word and char not in default:
            dict_word[char] = 1
        elif char in dict_word and char not in default:
            dict_word[char] += 1

sorted_dict = sorted(dict_word.items(), key=lambda x: x[1], reverse=True)
ans = 0

if K