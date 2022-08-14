alp = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in cro:
    if c in alp:
        alp = alp.replace(c, "*")

print(len(alp))





