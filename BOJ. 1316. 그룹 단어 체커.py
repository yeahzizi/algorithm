N = int(input())
alp = [input() for i in range(N)]
alp_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10,
            'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19,
            'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
cnt = [0] *26
ans = []

for i in range(N):
    for j in range(len(alp[i])):
        ans.append(alp[i][j])
    ans.append(1)

for i in ans:
    for key, value in alp_dict:
        if i == key:
            cnt[value] += 1





