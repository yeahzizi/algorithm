import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    mon = input()
    pokemon[mon] = i
    pokemon[i] = mon

for i in range(M):
    ans = input()
    if pokemon.get(ans) == None:
        print(pokemon.get(int(ans)))
    else:
        print(pokemon.get(ans))
