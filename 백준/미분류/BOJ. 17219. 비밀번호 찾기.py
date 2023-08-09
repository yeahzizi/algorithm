N, M = map(int, input().split())
secret = {}

for _ in range(N):
    site, password = input().split()
    secret[site] = password


for _ in range(M):
    site = input()
    print(secret.get(site))
