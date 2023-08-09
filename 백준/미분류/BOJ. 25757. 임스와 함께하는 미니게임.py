import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
player = []
for i in range(N):
    player.append(input())

player = set(player)
ans = 0

if game == "Y":
    ans = len(player)
elif game == "F":
    ans = len(player) // 2
elif game == "O":
    ans = len(player) // 3

print(ans)